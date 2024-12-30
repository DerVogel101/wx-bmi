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

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"BMI Rechner (KI DLC jetzt verfügbar)"), pos = wx.DefaultPosition, size = wx.Size( 692,390 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 700,400 ), wx.DefaultSize )

        content_box = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"BMI Rechner"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText8.SetMinSize( wx.Size( 250,55 ) )

        content_box.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.main_content_area = wx.BoxSizer( wx.HORIZONTAL )


        content_box.Add( self.main_content_area, 1, wx.EXPAND, 5 )


        self.SetSizer( content_box )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


