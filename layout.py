# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class bmiframe
###########################################################################

class bmiframe ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"BMI Rechner (KI DLC jetzt verfügbar)"), pos = wx.DefaultPosition, size = wx.Size( 688,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        gSizer2 = wx.GridSizer( 1, 2, 0, 0 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Körper Werte"), wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

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

        fgSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        radiobox_sexChoices = [ _(u"Männlich"), _(u"Weiblich"), _(u"keine Angabe") ]
        self.radiobox_sex = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), radiobox_sexChoices, 2, 0|wx.BORDER_NONE )
        self.radiobox_sex.SetSelection( 2 )
        fgSizer5.Add( self.radiobox_sex, 0, wx.SHAPED|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Größe: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer5.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_height = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        fgSizer5.Add( self.txt_height, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Gewicht: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_mass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        fgSizer5.Add( self.txt_mass, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.EXPAND, 5 )


        bSizer2.Add( fgSizer5, 1, wx.EXPAND, 5 )

        self.button_calc = wx.Button( self, wx.ID_ANY, _(u"Berechnen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.button_calc, 0, wx.ALL|wx.EXPAND, 5 )


        gSizer2.Add( bSizer2, 0, wx.SHAPED, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Ergebniss"), wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.bmi_table = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

        # Grid
        self.bmi_table.CreateGrid( 3, 3 )
        self.bmi_table.EnableEditing( True )
        self.bmi_table.EnableGridLines( True )
        self.bmi_table.EnableDragGridSize( False )
        self.bmi_table.SetMargins( 0, 0 )

        # Columns
        self.bmi_table.EnableDragColMove( False )
        self.bmi_table.EnableDragColSize( True )
        self.bmi_table.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.bmi_table.SetRowSize( 0, 27 )
        self.bmi_table.SetRowSize( 1, 26 )
        self.bmi_table.SetRowSize( 2, 27 )
        self.bmi_table.EnableDragRowSize( True )
        self.bmi_table.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.bmi_table.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer8.Add( self.bmi_table, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.img_green = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"indicator_gray.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.img_green.SetMinSize( wx.Size( 30,30 ) )

        bSizer10.Add( self.img_green, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 10 )

        self.img_yellow = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"indicator_gray.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.img_yellow.SetMinSize( wx.Size( 30,30 ) )

        bSizer10.Add( self.img_yellow, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 10 )

        self.img_red = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"indicator_gray.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.img_red.SetMinSize( wx.Size( 30,30 ) )

        bSizer10.Add( self.img_red, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 10 )


        bSizer3.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        wSizer1 = wx.WrapSizer( wx.HORIZONTAL, 0 )

        self.sadsg = wx.StaticText( self, wx.ID_ANY, _(u"Score:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sadsg.Wrap( -1 )

        self.sadsg.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.sadsg.SetMinSize( wx.Size( 55,20 ) )

        wSizer1.Add( self.sadsg, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT, 5 )

        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.m_textCtrl10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_textCtrl10.SetMinSize( wx.Size( 200,-1 ) )

        wSizer1.Add( self.m_textCtrl10, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer3.Add( wSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )


        gSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )


        bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


