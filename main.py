from openai import AuthenticationError, APIConnectionError

import wx
import wx.html2
import wx.lib
import layout.mainFrame as MainFrameModule
import layout.inputFrame as InputFrameModule
import layout.outputFrame as OutputFrameModule
import layout.aipopup as AiPopUpModule
import layout.airesponsepopup as AiResponsePopUpModule
import bmi_calculator

from ai_dlc import AiLib


shared_bmi = bmi_calculator.BmiCalc()
"""
Instance of the BmiCalc class from the bmi_calculator module.
Used to perform BMI calculations.
"""

EVT_BMI_UPDATE = wx.NewEventType()
"""
Custom event type for BMI updates.
"""

EVT_BMI_UPDATE_BINDER = wx.PyEventBinder(EVT_BMI_UPDATE)
"""
Binder for the custom BMI update event.
"""

class BmiUpdateEvent(wx.PyEvent):
    """
    Custom event class for BMI updates.

    Attributes:
        score (float): The BMI score to be updated.
    """
    def __init__(self, score):
        """
        Initializes the BmiUpdateEvent with the given BMI score.

        Args:
            score (float): The BMI score to be updated.
        """
        super().__init__()
        self.SetEventType(EVT_BMI_UPDATE)  # Set the event type
        self.score = score

class InputHandler(InputFrameModule.inputPanel):
    """
    Handles user input for BMI calculation.

    Inherits from:
        InputFrameModule.inputPanel: The input panel from the layout module.

    Attributes:
        ai_dlc (AiLib): Instance of the AiLib class for AI-related functionalities.
    """
    def __init__(self, parent):
        """
        Initializes the InputHandler with the given parent.

        Args:
            parent: The parent window.
        """
        super().__init__(parent)
        self.ai_dlc: AiLib = parent.ai_dlc
        self.button_calc.Bind(wx.EVT_BUTTON, self.on_calc)
        self.txt_age.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.txt_height.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.txt_mass.Bind(wx.EVT_CHAR, self.only_allow_float)
        self.Show()

    def only_allow_number(self, event):
        """
        Allows only numeric input for age and height fields.

        Args:
            event: The key event.
        """
        key_code = event.GetKeyCode()
        # Check if the key is a number, backspace, or a control key (e.g., arrow keys)
        if key_code in range(48, 58) or key_code in [wx.WXK_BACK, wx.WXK_RETURN]:
            event.Skip()  # Allow the input
        else:
            event.StopPropagation()  # Reject the input

    def only_allow_float(self, event):
        """
        Allows only numeric and float input for the mass field.

        Args:
            event: The key event.
        """
        key_code = event.GetKeyCode()
        # Check if the key is a number, backspace, comma, period, or a control key (e.g., arrow keys)
        if key_code in range(48, 58) or key_code in [wx.WXK_BACK, wx.WX_RETURN, wx.WXK_DECIMAL, wx.WXK_NUMPAD_DECIMAL, 44, 46]:
            if key_code == 44:  # If comma is pressed, replace it with a period
                event.GetEventObject().WriteText('.')
            else:
                event.Skip()  # Allow the input
        else:
            event.StopPropagation()  # Reject the input

    def on_calc(self, _):
        """
        Handles the calculation of BMI based on user input.

        Args:
            _: The event object (not used).
        """
        values = [0, 0, 0]
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
                    wx.MessageBox("Mit diesem Rechner können Sie den BMI ausschließlich für Personen ab 18 "
                                  "Jahren berechnen. Für Kinder probieren Sie bitte: "
                                  "https://www.cdc.gov/bmi/child-teen-calculator/index.html", "Error", wx.OK | wx.ICON_ERROR)
                    return
            except ValueError:
                wx.MessageBox(f"Ungültige eingabe für: {e.GetToolTip().GetTip()}", "Error", wx.OK | wx.ICON_ERROR)
                return

        # Get Sex
        try:
            match self.radiobox_sex.GetStringSelection()[0]:
                case 'M':
                    shared_bmi.set_sex("m")
                    self.ai_dlc.sex = "Männlich"
                case 'W':
                    shared_bmi.set_sex("f")
                    self.ai_dlc.sex = "Weiblich"
                case _:
                    shared_bmi.set_sex(None)
                    self.ai_dlc.sex = "keine Angabe"
        except bmi_calculator.SexError as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        # Get Body Type
        try:
            match self.radiobox_body_type.GetStringSelection()[0]:
                case 'Z':
                    shared_bmi.set_body_type("s")
                    self.ai_dlc.btype = "Zierlich"
                case 'N':
                    shared_bmi.set_body_type("M")
                    self.ai_dlc.btype = "Normal"
                case 'K':
                    shared_bmi.set_body_type("L")
                    self.ai_dlc.btype = "Kräftig"
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

            self.ai_dlc.age = str(values[0])
            self.ai_dlc.height = str(values[1])
            self.ai_dlc.weigth = str(values[2])
            self.ai_dlc.bmi_score = str(score)
        except Exception as e:
            wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            return

        wx.PostEvent(self.GetParent(), BmiUpdateEvent(score))


class OutputFrame(OutputFrameModule.outputPanel):
    """
    Output frame class for displaying BMI results.

    Inherits from:
        OutputFrameModule.outputPanel: The output panel from the layout module.
    """
    def __init__(self, parent):
        """
        Initializes the OutputFrame with the given parent.

        Args:
            parent: The parent window.
        """
        super().__init__(parent)
        self.bmi_table.SetRowLabelSize(300)
        # self.bmi_table.SetDefaultRowSize(100)
        self.Show()


class AiPopUp(AiPopUpModule.AiPopUp):
    """
    Popup dialog for AI settings.

    Inherits from:
        AiPopUpModule.AiPopUp: The base popup class from the layout module.

    Attributes:
        parent: The parent window.
        close_source (str): The source of the close event.
    """
    def __init__(self, parent):
        """
        Initializes the AiPopUp with the given parent.

        Args:
            parent: The parent window.
        """
        super().__init__(parent)
        self.parent = parent
        self.close_source = None

    def deny_ai(self, event):
        """
        Disables AI functionality and closes the popup.

        Args:
            event: The event object.
        """
        self.close_source = 'deny'
        self.parent.enable_ai = False
        self.Close()
        event.Skip()

    def shutdown_prog(self, event):
        """
        Shuts down the program if the close source is not 'continue' or 'deny'.

        Args:
            event: The event object.
        """
        if self.close_source == 'continue' or self.close_source == 'deny':
            event.Skip()
        else:
            wx.Exit()

    def continue_prog(self, event):
        """
        Continues the program with AI enabled and closes the popup.

        Args:
            event: The event object.
        """
        self.parent.ai_dlc.set_api_key(self.ai_key_field.GetValue())
        self.parent.ai_dlc.personallity = self.ai_personality.GetValue()
        self.close_source = 'continue'
        self.Close()
        event.Skip()


class AiResponsePopUp(AiResponsePopUpModule.AiResponsePopUp):
    """
    Popup dialog for displaying AI responses.

    Inherits from:
        AiResponsePopUpModule.AiResponsePopUp: The base popup class from the layout module.

    Attributes:
        parent: The parent window.
        m_htmlWin1: The WebView control for displaying HTML content.
        sizer: The sizer for managing the layout of the popup.
    """
    def __init__(self, parent):
        """
        Initializes the AiResponsePopUp with the given parent.

        Args:
            parent: The parent window.
        """
        super().__init__(parent)
        self.parent = parent
        self.m_htmlWin1 = wx.html2.WebView.New(self)  # Replace HtmlWindow with WebView
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.m_htmlWin1, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

    def set_html_content(self, html_content):
        """
        Sets the HTML content to be displayed in the WebView.

        Args:
            html_content (str): The HTML content to display.
        """
        self.m_htmlWin1.SetPage(html_content, "")
        self.m_htmlWin1.Refresh()


class MainFrame(MainFrameModule.bmiMainFrame):
    """
    Main frame class for the BMI application.

    Inherits from:
        MainFrameModule.bmiMainFrame: The base main frame class from the layout module.

    Attributes:
        ai_dlc (AiLib): Instance of the AiLib class for AI-related functionalities.
        enable_ai (bool): Flag to enable or disable AI functionalities.
        input_frame (InputHandler): Instance of the InputHandler class for handling user input.
        output_frame (OutputFrame): Instance of the OutputFrame class for displaying BMI results.
        ai_dialog (AiPopUp): Instance of the AiPopUp class for AI settings popup.
        ai_response_dialog (AiResponsePopUp): Instance of the AiResponsePopUp class for displaying AI responses.
    """
    def __init__(self, parent):
        """
        Initializes the MainFrame with the given parent.

        Args:
            parent: The parent window.
        """
        super().__init__(parent)
        self.ai_dlc = AiLib()
        self.enable_ai = True

        self.input_frame = InputHandler(self)
        self.output_frame = OutputFrame(self)
        self.ai_dialog = AiPopUp(self)
        self.ai_response_dialog = AiResponsePopUp(self)

        self.main_content_area.Add(self.input_frame, 1, wx.EXPAND)
        self.main_content_area.Add(self.output_frame, 1, wx.EXPAND)

        self.Bind(EVT_BMI_UPDATE_BINDER, self.on_bmi_update)
        self.Show()

        self.ai_dialog.ShowModal()

    def on_bmi_update(self, event):
        """
        Handles the BMI update event.

        Args:
            event: The BMI update event object.
        """
        # Update score
        self.output_frame.score_box.SetValue(str(event.score))
        # Update ideal weight
        try:
            self.output_frame.ideal_weight_box.SetValue(str(shared_bmi.get_ideal_weight()))
            self.ai_dlc.craff_score = str(shared_bmi.get_ideal_weight())
        except bmi_calculator.AgeDiscriminationError:
            self.output_frame.ideal_weight_box.SetValue(str("Alter benötigt"))

        # Get table
        table = shared_bmi.bmi_cat.selected_categories
        # Clear table, adjust size
        # Technically not needed but allows for changes in table without needing to touch this code
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

        self.ai_dlc.bmi_cat = shared_bmi.bmi_cat[event.score][0]
        self.ai_dlc.assemble_messages()

        self.output_frame.bmi_table.Enable(True)

        if self.enable_ai:
            self.SetCursor(wx.Cursor(wx.CURSOR_WAIT))  # Set wait cursor
            try:
                response = self.ai_dlc.get_response()
            except (AuthenticationError, APIConnectionError):
                wx.MessageBox("API Key ungültig", "Error", wx.OK | wx.ICON_ERROR)
                self.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))  # Reset cursor on error
                return
            self.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))  # Reset cursor after response
            self.ai_response_dialog.set_html_content(str(response.content))
            self.ai_response_dialog.Show()


if __name__ == '__main__':
    """
    Entry point for the BMI application.
    """
    app = wx.App()
    """
    Creates an instance of the wx.App class, which initializes the application.
    """
    root = MainFrame(None)
    """
    Creates an instance of the MainFrame class, which is the main window of the application.
    
    Args:
        None: The parent window (None indicates no parent).
    """
    app.MainLoop()
    """
    Starts the main event loop, which waits for user interaction and handles events.
    """
