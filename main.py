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
        self.txt_age.Bind(wx.EVT_TEXT, self.update_age)
        self.radiobox_sex.Bind(wx.EVT_RADIOBOX, self.update_sex)
        self.txt_height.Bind(wx.EVT_TEXT, self.update_height)
        self.txt_mass.Bind(wx.EVT_TEXT, self.update_weight)
        self.Show()

    def on_calc(self, event):
        pass

    def update_age(self, event):
        pass

    def update_sex(self, event):
        pass

    def update_height(self, event):
        pass

    def update_weight(self, event):
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

