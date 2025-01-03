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
## Class AiPopUp
###########################################################################

class AiPopUp ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"AI DLC Einstellungen"), pos = wx.DefaultPosition, size = wx.Size( 520,160 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

        self.SetSizeHints( wx.Size( 520,160 ), wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"Das DLC Benötigt einen OpenAI API Schlüssel, \num Ihre Daten an OpenAI zu senden und sie zuverarbeiten"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer9.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.ai_key_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer9.Add( self.ai_key_field, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.cancel_butt = wx.Button( self, wx.ID_ANY, _(u"Abbrechen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.cancel_butt, 0, wx.ALL, 5 )

        self.continue_butt = wx.Button( self, wx.ID_ANY, _(u"Weiter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.continue_butt, 0, wx.ALL, 5 )


        bSizer9.Add( bSizer10, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.shutdown_prog )
        self.cancel_butt.Bind( wx.EVT_BUTTON, self.shutdown_prog )
        self.continue_butt.Bind( wx.EVT_BUTTON, self.continue_prog )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def shutdown_prog( self, event ):
        event.Skip()


    def continue_prog( self, event ):
        event.Skip()


