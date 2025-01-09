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
## Class inputPanel
###########################################################################

class inputPanel ( wx.Panel ):
    """
    A panel class for inputting body measurements and other related data.

    Inherits from:
        wx.Panel: The base class for all panels in wxPython.
    """

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        """
        Initializes the inputPanel with various input fields and labels.

        Args:
            parent (wx.Window): The parent window for this panel.
            id (int, optional): The window identifier. Defaults to wx.ID_ANY.
            pos (wx.Point, optional): The position of the panel. Defaults to wx.DefaultPosition.
            size (wx.Size, optional): The size of the panel. Defaults to wx.Size(-1, -1).
            style (int, optional): The window style. Defaults to wx.TAB_TRAVERSAL.
            name (str, optional): The name of the panel. Defaults to wx.EmptyString.
        """
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Körper Werte:"), wx.DefaultPosition, wx.Size( 145,30 ), 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, _(u"Alter:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        fgSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_age = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        fgSizer5.Add( self.txt_age, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Geschlecht: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        fgSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        radiobox_sexChoices = [ _(u"Männlich"), _(u"Weiblich"), _(u"keine Angabe") ]
        self.radiobox_sex = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), radiobox_sexChoices, 2, 0|wx.BORDER_NONE )
        self.radiobox_sex.SetSelection( 2 )
        fgSizer5.Add( self.radiobox_sex, 0, wx.SHAPED|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )

        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, _(u"Körpertypen:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )

        fgSizer5.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        radiobox_body_typeChoices = [ _(u"Zierlich"), _(u"Normal"), _(u"Kräftig") ]
        self.radiobox_body_type = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), radiobox_body_typeChoices, 2, 0|wx.BORDER_NONE )
        self.radiobox_body_type.SetSelection( 1 )
        fgSizer5.Add( self.radiobox_body_type, 0, wx.BOTTOM, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Größe (cm): "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer5.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_height = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        self.txt_height.SetToolTip( _(u"Größe") )

        fgSizer5.Add( self.txt_height, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Gewicht (kg): "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_mass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        self.txt_mass.SetToolTip( _(u"Gewicht") )

        fgSizer5.Add( self.txt_mass, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.RIGHT, 5 )

        bSizer2.Add( fgSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.button_calc = wx.Button( self, wx.ID_ANY, _(u"Berechnen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.button_calc, 0, wx.ALL|wx.EXPAND, 5 )

        self.SetSizer( bSizer2 )
        self.Layout()
        bSizer2.Fit( self )

    def __del__( self ):
        """
        Destructor for the inputPanel class.
        """
        pass


