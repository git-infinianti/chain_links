# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Helper
###########################################################################

class Helper ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"A blockchain coin.conf injector.", pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Config Helper", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 36, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Unispace" ) )

        bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Chain", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"raven", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl1.SetToolTip( u"Specify a chain this config is for.\nNeeded if default paths are used." )

        bSizer4.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 0, 4, 0, 0 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Run Testnet", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Testnet", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn1.SetToolTip( u"Run on the test network instead of the real network." )

        gSizer1.Add( self.m_toggleBtn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Run Regtest", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn2 = wx.ToggleButton( self, wx.ID_ANY, u"Regtest", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn2.SetToolTip( u"Run a regression test network." )

        gSizer1.Add( self.m_toggleBtn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"RPC Server", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn3 = wx.ToggleButton( self, wx.ID_ANY, u"Serve", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn3.SetValue( True )
        self.m_toggleBtn3.SetToolTip( u"Tells Chain-Qt and chaind to accept JSON-RPC commands." )

        gSizer1.Add( self.m_toggleBtn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Start Minimized", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn4 = wx.ToggleButton( self, wx.ID_ANY, u"Minimize", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn4.SetValue( True )
        self.m_toggleBtn4.SetToolTip( u"Start Chain-QT minimized." )

        gSizer1.Add( self.m_toggleBtn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Close To Tray", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn5 = wx.ToggleButton( self, wx.ID_ANY, u"Tray", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn5.SetValue( True )
        self.m_toggleBtn5.SetToolTip( u"Minimize to the system tray." )

        gSizer1.Add( self.m_toggleBtn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Transaction Index", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn6 = wx.ToggleButton( self, wx.ID_ANY, u"TX", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn6.SetValue( True )
        self.m_toggleBtn6.SetToolTip( u"Maintains the full Transaction index on your node. \nNeeded if you call getrawtransaction." )

        gSizer1.Add( self.m_toggleBtn6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Address Index", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn7 = wx.ToggleButton( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn7.SetValue( True )
        self.m_toggleBtn7.SetToolTip( u"Maintains the full Address index on your node. \nNeeded if you call getaddress." )

        gSizer1.Add( self.m_toggleBtn7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Asset Index", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn8 = wx.ToggleButton( self, wx.ID_ANY, u"Asset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn8.SetValue( True )
        self.m_toggleBtn8.SetToolTip( u"Maintains the full Asset index on your node. \nNeeded if you call getassetdata." )

        gSizer1.Add( self.m_toggleBtn8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Timestamp Index", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        self.m_staticText11.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn9 = wx.ToggleButton( self, wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn9.SetValue( True )
        self.m_toggleBtn9.SetToolTip( u"Maintains the full Timestamp index on your node." )

        gSizer1.Add( self.m_toggleBtn9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Spent Index", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        self.m_staticText12.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        gSizer1.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_toggleBtn10 = wx.ToggleButton( self, wx.ID_ANY, u"Spent", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn10.SetValue( True )
        self.m_toggleBtn10.SetToolTip( u"Maintains the full Spent index on your node." )

        gSizer1.Add( self.m_toggleBtn10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        gSizer2 = wx.GridSizer( 0, 4, 0, 1 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Max Connections:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        gSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2.SetToolTip( u"Maximum number of inbound+outbound connections." )

        gSizer2.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Bind IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetToolTip( u"Bind to given address and always listen on it. \nUse [host]:port notation for IPv6" )

        gSizer2.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Whitebind IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        gSizer2.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl4.SetToolTip( u"Bind to given address and whitelist peers connecting to it. \nUse [host]:port notation for IPv6" )

        gSizer2.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Proxy IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        gSizer2.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl5.SetToolTip( u"Connect via a SOCKS5 proxy." )

        gSizer2.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 0, 8, 0, 0 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"RPC Connect:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        gSizer3.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"127.0.0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl6.SetToolTip( u"You can use Chaincoin or chaincoind to send commands to Chaincoin/chaincoind running on another host using this option.\\ndefault = 127.0.0.1" )

        gSizer3.Add( self.m_textCtrl6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"RPC User:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        gSizer3.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl7.SetToolTip( u"Username to send RPC commands." )

        gSizer3.Add( self.m_textCtrl7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"RPC Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        gSizer3.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl8.SetToolTip( u"Password to send RPC commands." )

        gSizer3.Add( self.m_textCtrl8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"RPC Client Timeout:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        gSizer3.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl9.SetToolTip( u"How many seconds the server will wait for a complete RPC HTTP request." )

        gSizer3.Add( self.m_textCtrl9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"RPC Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        gSizer3.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"8766", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl10.SetToolTip( u"Listen for RPC connections on this TCP port." )

        gSizer3.Add( self.m_textCtrl10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Wallet Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        gSizer3.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL )
        self.m_dirPicker1.SetToolTip( u"Specify where to find wallet, lockfile and logs. \nIf not present, those files will be created as new.\nIf not specified defaults will be used." )

        gSizer3.Add( self.m_dirPicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Data Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        gSizer3.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL )
        self.m_dirPicker2.SetToolTip( u"Specify where to find database, blocks and chainstate. \nIf not present, those files will be created as new.\nIf not specified defaults will be used." )

        gSizer3.Add( self.m_dirPicker2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"TX Confirm Target:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        gSizer3.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl11.SetToolTip( u"Create transactions that have enough fees so they are likely to begin confirmation within n blocks (default: 6).\n" )

        gSizer3.Add( self.m_textCtrl11, 0, wx.ALL, 5 )


        bSizer2.Add( gSizer3, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Keypool:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        bSizer5.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl12.SetToolTip( u"Pre-generate this many public/private key pairs, so wallet backups will be valid for both prior transactions and several dozen future transactions." )

        bSizer5.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Prune:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        bSizer5.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl13.SetToolTip( u"Enable pruning to reduce storage requirements by deleting old blocks.\nThis mode is incompatible with -txindex and -rescan.\n0 = default (no pruning).\n1 = allows manual pruning via RPC.\n550 = target to stay under in MiB." )

        bSizer5.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Pay TX Fee:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        bSizer5.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl14.SetToolTip( u"Pay an optional transaction fee every time you send coins." )

        bSizer5.Add( self.m_textCtrl14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer2.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 100, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.SetColSize( 0, 97 )
        self.m_grid1.SetColSize( 1, 144 )
        self.m_grid1.SetColSize( 2, 159 )
        self.m_grid1.SetColSize( 3, 146 )
        self.m_grid1.SetColSize( 4, 149 )
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelValue( 0, u"Nodes" )
        self.m_grid1.SetColLabelValue( 1, u"Connections" )
        self.m_grid1.SetColLabelValue( 2, u"RPC Binds" )
        self.m_grid1.SetColLabelValue( 3, u"RPC Allowed IPs" )
        self.m_grid1.SetColLabelValue( 4, u"Authentications" )
        self.m_grid1.SetColLabelValue( 5, wx.EmptyString )
        self.m_grid1.SetColLabelValue( 6, wx.EmptyString )
        self.m_grid1.SetColLabelValue( 7, wx.EmptyString )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer6.Add( self.m_grid1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer1.Add( bSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl15.Hide()

        bSizer1.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

        self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl16.Hide()

        bSizer1.Add( self.m_textCtrl16, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnSubmitClick )
        self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.OnListDataChanged )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnSubmitClick( self, event ):
        pass

    def OnListDataChanged( self, event ):
        pass


