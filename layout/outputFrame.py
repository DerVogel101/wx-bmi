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
    """
    A panel class for displaying BMI results and related information.

    Inherits from:
        wx.Panel: The base class for all panels in wxPython.
    """

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        """
        Initializes the outputPanel with various static texts, a grid for BMI data, and text controls.

        Args:
            parent (wx.Window): The parent window for this panel.
            id (int, optional): The window identifier. Defaults to wx.ID_ANY.
            pos (wx.Point, optional): The position of the panel. Defaults to wx.DefaultPosition.
            size (wx.Size, optional): The size of the panel. Defaults to wx.Size(-1, -1).
            style (int, optional): The window style. Defaults to wx.TAB_TRAVERSAL.
            name (str, optional): The name of the panel. Defaults to wx.EmptyString.
        """
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Ergebniss:"), wx.DefaultPosition, wx.Size( -1,30 ), 0 )
        self.m_staticText18.Wrap( -1 )

        self.m_staticText18.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.m_staticText18.SetMinSize( wx.Size( 110,30 ) )

        bSizer8.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer71 = wx.BoxSizer( wx.VERTICAL )

        self.bmi_table = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.FULL_REPAINT_ON_RESIZE )

        # Grid
        self.bmi_table.CreateGrid( 6, 2 )
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

        bSizer71.Add( self.bmi_table, 0, 0, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"*angaben in BMI-Score"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.m_staticText13.SetMinSize( wx.Size( -1,20 ) )

        bSizer71.Add( self.m_staticText13, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer71, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Idealgewicht (kg):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer81.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ideal_weight_box = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer81.Add( self.ideal_weight_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer81, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer82 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"*berechnet mit der Creff Formel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer82.Add( self.m_staticText12, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer82, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.sadsg = wx.StaticText( self, wx.ID_ANY, _(u"BMI-Score:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sadsg.Wrap( -1 )

        self.sadsg.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.sadsg.SetMinSize( wx.Size( 140,30 ) )

        bSizer12.Add( self.sadsg, 0, wx.ALIGN_BOTTOM|wx.LEFT, 5 )


        bSizer8.Add( bSizer12, 1, wx.BOTTOM, 5 )

        self.score_box = wx.TextCtrl( self, wx.ID_ANY, _(u"n/a"), wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.score_box.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.score_box.SetMinSize( wx.Size( 200,-1 ) )

        bSizer8.Add( self.score_box, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()
        bSizer8.Fit( self )

    def __del__( self ):
        """
        Destructor for the outputPanel class.
        """
        pass


