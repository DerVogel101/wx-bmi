import wx
import layout.mainFrame as MainFrameModule
import layout.inputFrame as InputFrameModule
import layout.outputFrame as OutputFrameModule
import bmi_calculator


shared_bmi = bmi_calculator.BmiCalc()


class InputHandler(InputFrameModule.inputPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.button_calc.Bind(wx.EVT_BUTTON, self.on_calc)
        self.txt_age.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.radiobox_sex.Bind(wx.EVT_RADIOBOX, self.update_sex)
        self.txt_height.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.txt_mass.Bind(wx.EVT_CHAR, self.only_allow_number)
        self.Show()

    def only_allow_number(self, event):
        key_code = event.GetKeyCode()
        # Check if the key is a number, backspace, or a control key (e.g., arrow keys)
        if (48 <= key_code <= 57) or (key_code in [wx.WXK_BACK, wx.WXK_RETURN]):
            event.Skip()  # Allow the input
        else:
            event.Veto()  # Reject the input

    def update_sex(self, event):
        pass

    def on_calc(self, event):
        pass


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
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    root = MainFrame(None)
    app.MainLoop()

