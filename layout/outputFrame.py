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
## Class outputPanel
###########################################################################

class outputPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        gSizer2 = wx.GridSizer( 1, 2, 0, 0 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Ergebniss"), wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText18.Wrap( -1 )

        self.m_staticText18.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.m_staticText18, 0, wx.ALL|wx.EXPAND, 5 )

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
        bSizer8.Add( self.bmi_table, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer8, 1, wx.ALIGN_CENTER, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

        self.sadsg = wx.StaticText( self, wx.ID_ANY, _(u"Score:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sadsg.Wrap( -1 )

        self.sadsg.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.sadsg.SetMinSize( wx.Size( 55,20 ) )

        gSizer5.Add( self.sadsg, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT, 5 )

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


        gSizer5.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer12.Add( gSizer5, 0, wx.EXPAND, 5 )

        self.score_box = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.score_box.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.score_box.SetMinSize( wx.Size( 200,-1 ) )

        bSizer12.Add( self.score_box, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer3.Add( bSizer12, 0, wx.BOTTOM, 5 )


        gSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )


        self.SetSizer( gSizer2 )
        self.Layout()

    def __del__( self ):
        pass


