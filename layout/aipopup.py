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
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"AI DLC Einstellungen"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"Das DLC Benötigt einen OpenAI API Schlüssel, \num Ihre Daten an OpenAI zu senden und sie zuverarbeiten"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText13.SetMinSize( wx.Size( 600,70 ) )

        bSizer9.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.ai_key_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer9.Add( self.ai_key_field, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Persöhnlichkeit der Ai bestimmen:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText14.Wrap( -1 )

        self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer12.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, _(u"Schreibe die Antwort"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        bSizer13.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.ai_personality = wx.TextCtrl( self, wx.ID_ANY, _(u"als wärst du ein Fitness Influenzer"), wx.DefaultPosition, wx.DefaultSize, wx.TE_BESTWRAP )
        bSizer13.Add( self.ai_personality, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer13.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer9.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.cancel_butt = wx.Button( self, wx.ID_ANY, _(u"Abbrechen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.cancel_butt, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.continue_butt = wx.Button( self, wx.ID_ANY, _(u"Weiter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.continue_butt, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer9.Add( bSizer10, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()
        bSizer9.Fit( self )

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


