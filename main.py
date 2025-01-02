import wx
import wx.lib
import layout.mainFrame as MainFrameModule
import layout.inputFrame as InputFrameModule
import layout.outputFrame as OutputFrameModule
import bmi_calculator


shared_bmi = bmi_calculator.BmiCalc()

EVT_BMI_UPDATE = wx.NewEventType()
EVT_BMI_UPDATE_BINDER = wx.PyEventBinder(EVT_BMI_UPDATE)

class BmiUpdateEvent(wx.PyEvent):
    def __init__(self, score):
        super().__init__()
        self.SetEventType(EVT_BMI_UPDATE)  # Set the event type
        self.score = score

class InputHandler(InputFrameModule.inputPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.button_calc.Bind(wx.EVT_BUTTON, self.on_calc)
        self.txt_age.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.txt_height.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.txt_mass.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.Show()

    def only_allow_number(self, event):
        key_code = event.GetKeyCode()
        # Check if the key is a number, backspace, or a control key (e.g., arrow keys)
        if (48 <= key_code <= 57) or (key_code in [wx.WXK_BACK, wx.WXK_RETURN]):
            event.Skip()  # Allow the input
        else:
            event.StopPropagation()  # Reject the input

    def on_calc(self, _):
        values = [0,0,0]
        for i, e in enumerate([self.txt_age, self.txt_height, self.txt_mass]):
            try:
                # Edge cases Age
                ### Empty input
                if i == 0 and not e.GetValue():
                    values[i] = None
                    continue
                values[i] = float(e.GetValue())
                ### Underage
                if i == 0 and values[i] < 18:
                    wx.MessageBox("Mit diesem Rechner können Sie den BMI ausschließlich für Personen ab 18 \
Jahren berechnen. Für Kinder probieren Sie bitte: \
https://www.cdc.gov/bmi/child-teen-calculator/index.html", "Error", wx.OK | wx.ICON_ERROR)
                    return
            except ValueError:
                wx.MessageBox(f"Ungültige eingabe für: {e.GetToolTip().GetTip()}", "Error", wx.OK | wx.ICON_ERROR)
                return
        
        # Get Sex
        try:
            match self.radiobox_sex.GetStringSelection()[0]:
                case 'M':
                    shared_bmi.set_sex("m")
                case 'W':
                    shared_bmi.set_sex("f")
                case _:
                    shared_bmi.set_sex(None)
        except bmi_calculator.SexError as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        # Get Body Type
        try:
            match self.radiobox_body_type.GetStringSelection()[0]:
                case 'Z':
                    shared_bmi.set_body_type("s")
                case 'N':
                    shared_bmi.set_body_type("M")
                case 'K':
                    shared_bmi.set_body_type("L")
                case _:
                    pass # This can never happen
        except Exception as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        # Set Int values and calculate
        try:
            shared_bmi.set_age(values[0])
            shared_bmi.set_size(values[1] / 100) # Convert cm to m
            shared_bmi.set_weight(values[2])
            score = shared_bmi.get_bmi()
        except Exception as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        wx.PostEvent(self.GetParent(), BmiUpdateEvent(score))


class OutputFrame(OutputFrameModule.outputPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.bmi_table.SetRowLabelSize(300)
        #self.bmi_table.SetDefaultRowSize(100)
        self.Show()


class MainFrame(MainFrameModule.bmiMainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.input_frame = InputHandler(self)
        self.output_frame = OutputFrame(self)
        self.main_content_area.Add(self.input_frame, 1, wx.EXPAND)
        self.main_content_area.Add(self.output_frame, 1, wx.EXPAND)

        self.Bind(EVT_BMI_UPDATE_BINDER, self.on_bmi_update)
        self.Show()

    def on_bmi_update(self, event):
        # Update score 
        self.output_frame.score_box.SetValue(str(event.score))
        # Update ideal weight
        try:
            self.output_frame.ideal_weight_box.SetValue(str(shared_bmi.get_ideal_weight()))
        except bmi_calculator.AgeDiscriminationError:
            self.output_frame.ideal_weight_box.SetValue(str("Alter benötigt"))

        # Get table
        table = shared_bmi.bmi_cat.selected_categories
        # Clear table, adjust size
        # Technically not needed but alows for changes in table without needing to touch this code
        self.output_frame.bmi_table.ClearGrid()
        # Update col headers
        self.output_frame.bmi_table.SetColLabelValue(0, "Von")
        self.output_frame.bmi_table.SetColLabelValue(1, "Bis")
        # Update row 
        for i, e in enumerate(table):
            self.output_frame.bmi_table.SetRowLabelValue(i, e[0])
            self.output_frame.bmi_table.SetCellValue(i, 0, str(e[1][0]).replace("None", "-"))
            self.output_frame.bmi_table.SetCellValue(i, 1, str(e[1][1]).replace("None", "-"))
            min_val = e[1][0] if e[1][0] is not None else float('-inf')
            max_val = e[1][1] if e[1][1] is not None else float('inf')
            col = None
            if min_val <= event.score <= max_val:
                # Highlight the row, that the score is in
                col = wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT)
            else:
                # Reset color from previous highlighting
                col = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
            self.output_frame.bmi_table.SetCellBackgroundColour(i, 0, col)
            self.output_frame.bmi_table.SetCellBackgroundColour(i, 1, col)

        self.output_frame.bmi_table.Enable(True)

        
if __name__ == '__main__':
    app = wx.App()
    root = MainFrame(None)
    app.MainLoop()

