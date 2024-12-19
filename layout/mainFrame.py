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

        content_box = wx.BoxSizer( wx.HORIZONTAL )


        self.SetSizer( content_box )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


