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

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Ergebniss:"), wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText18.Wrap( -1 )

        self.m_staticText18.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText18.SetMinSize( wx.Size( 110,30 ) )

        bSizer8.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.bmi_table = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

        # Grid
        self.bmi_table.CreateGrid( 10, 2 )
        self.bmi_table.EnableEditing( False )
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
        self.bmi_table.AutoSizeRows()
        self.bmi_table.EnableDragRowSize( True )
        self.bmi_table.SetRowLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.bmi_table.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.bmi_table.Enable( False )

        bSizer8.Add( self.bmi_table, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Idealgewicht (kg):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer81.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ideal_weight_box = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer81.Add( self.ideal_weight_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer81, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.sadsg = wx.StaticText( self, wx.ID_ANY, _(u"Score:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sadsg.Wrap( -1 )

        self.sadsg.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.sadsg.SetMinSize( wx.Size( 70,30 ) )

        bSizer12.Add( self.sadsg, 0, wx.BOTTOM|wx.LEFT|wx.ALIGN_BOTTOM, 5 )


        bSizer8.Add( bSizer12, 1, wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.score_box = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.score_box.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.score_box.SetMinSize( wx.Size( 200,-1 ) )

        bSizer8.Add( self.score_box, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()
        bSizer8.Fit( self )

    def __del__( self ):
        pass


