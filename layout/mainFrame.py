# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class bmiMainFrame
###########################################################################

class bmiMainFrame ( wx.Frame ):
    """
    A frame class for the main window of the BMI calculator application.

    Inherits from:
        wx.Frame: The base class for all frames in wxPython.
    """

    def __init__( self, parent ):
        """
        Initializes the bmiMainFrame with a title, size, and various UI components.

        Args:
            parent (wx.Window): The parent window for this frame.
        """
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"BMI Rechner AI-DLC"), pos = wx.DefaultPosition, size = wx.Size( 1000,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 790,460 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        content_box = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"BMI Rechner + AI"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText8.SetMinSize( wx.Size( 350,55 ) )

        content_box.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.main_content_area = wx.BoxSizer( wx.HORIZONTAL )

        self.main_content_area.SetMinSize( wx.Size( -1,800 ) )

        content_box.Add( self.main_content_area, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.SetSizer( content_box )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        """
        Destructor for the bmiMainFrame class.
        """
        pass


