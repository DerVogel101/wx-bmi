import wx
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
                values[i] = float(e.GetValue())
            except ValueError:
                wx.MessageBox(f"Invalid input for {e.GetToolTip()}", "Error", wx.OK | wx.ICON_ERROR)
                return
        
        try:
            match self.radiobox_sex.GetStringSelection()[0]:
                case 'Mänlich': shared_bmi.set_sex("m")
                case 'Weiblich': shared_bmi.set_sex("f")
                case _:  shared_bmi.set_sex(None)

        except bmi_calculator.SexError as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        try:
            shared_bmi.set_age(values[0])
            shared_bmi.set_size(values[1])
            shared_bmi.set_weight(values[2])
            score = shared_bmi.get_bmi()
        except Exception as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        wx.PostEvent(self.GetParent(), BmiUpdateEvent(score))


class OutputFrame(OutputFrameModule.outputPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()


class MainFrame(MainFrameModule.bmiMainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.input_frame = InputHandler(self)
        self.output_frame = OutputFrame(self)
        self.Sizer.Add(self.input_frame, 1, wx.EXPAND)
        self.Sizer.Add(self.output_frame, 1, wx.EXPAND)

        self.Bind(EVT_BMI_UPDATE_BINDER, self.on_bmi_update)
        self.Show()

    def on_bmi_update(self, event):
        print(event.score)
        self.output_frame.score_box.SetValue(str(event.score))


if __name__ == '__main__':
    app = wx.App()
    root = MainFrame(None)
    app.MainLoop()

