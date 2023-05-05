import wx
import Config
import NodeSetup


class Helper(Config.Helper):
    def __init__(self, parent):
        Helper.__init__(self, parent)
        self.gridCoords = {
            'nodes': [],
            'connections': [],
            'rpcbinds': [],
            'rpcallowedips': [],
            'authentications': []
        }

    def OnSubmitClick(self, event):
        chain = self.m_textCtrl1.GetValue()
        maxConnections = self.m_textCtrl2.GetValue()
        bind = self.m_textCtrl3.GetValue()
        whitebind = self.m_textCtrl4.GetValue()
        proxy = self.m_textCtrl5.GetValue()
        rpcConnect = self.m_textCtrl6.GetValue()
        rpcUser = self.m_textCtrl7.GetValue()
        rpcPass = self.m_textCtrl8.GetValue()
        rpcClientTimeOut = self.m_textCtrl9.GetValue()
        rpcPort = self.m_textCtrl10.GetValue()
        txConfirmTarget = self.m_textCtrl11.GetValue()
        keypool = self.m_textCtrl12.GetValue()
        prune = self.m_textCtrl13.GetValue()
        payTXFee = self.m_textCtrl14.GetValue()

        testnet = 1 if self.m_toggleBtn1.GetValue() else 0
        regtest = 1 if self.m_toggleBtn2.GetValue() else 0
        server = 1 if self.m_toggleBtn3.GetValue() else 0
        minimized = 1 if self.m_toggleBtn4.GetValue() else 0
        toTray = 1 if self.m_toggleBtn5.GetValue() else 0
        txIndex = 1 if self.m_toggleBtn6.GetValue() else 0
        addressIndex = 1 if self.m_toggleBtn7.GetValue() else 0
        assetIndex = 1 if self.m_toggleBtn8.GetValue() else 0
        timestampIndex = 1 if self.m_toggleBtn9.GetValue() else 0
        spentIndex = 1 if self.m_toggleBtn10.GetValue() else 0
        walletPath = self.m_dirPicker1.GetTextCtrl().GetValue()
        dataPath = self.m_dirPicker2.GetTextCtrl().GetValue()

        nodes = []
        connections = []
        rpcBinds = []
        rpcAllowedIPs = []
        authentications = []

        for row in self.gridCoords.values():
            for cell in row:
                match cell[1]:
                    case 0: nodes.append(self.m_grid1.GetCellValue(cell))
                    case 1: connections.append(self.m_grid1.GetCellValue(cell))
                    case 2: rpcBinds.append(self.m_grid1.GetCellValue(cell))
                    case 3: rpcAllowedIPs.append(self.m_grid1.GetCellValue(cell))
                    case 4: authentications.append(self.m_grid1.GetCellValue(cell))
        print(nodes, connections, rpcBinds, rpcAllowedIPs, authentications)
        listen = 0 if connections else 1

        NodeSetup.generate_conf(
            chain, testnet, regtest, proxy, bind, whitebind, nodes, connections, listen, maxConnections, server, rpcBinds, authentications,
            rpcUser, rpcPass, rpcClientTimeOut, rpcAllowedIPs, None, rpcPort, walletPath, dataPath, rpcConnect, txConfirmTarget, keypool, payTXFee,
            prune, minimized, toTray, txIndex, addressIndex, assetIndex, timestampIndex, spentIndex
        )

    def OnListDataChanged(self, event):
        coord = self.m_grid1.GetGridCursorCoords()
        match coord[1]:
            case 0:
                if coord not in self.gridCoords['nodes']:
                    self.gridCoords['nodes'] += [coord]
            case 1:
                if coord not in self.gridCoords['connections']:
                    self.gridCoords['connections'] += [coord]
            case 2:
                if coord not in self.gridCoords['rpcbinds']:
                    self.gridCoords['rpcbinds'] += [coord]
            case 3:
                if coord not in self.gridCoords['rpcallowedips']:
                    self.gridCoords['rpcallowedips'] += [coord]
            case 4:
                if coord not in self.gridCoords['authentications']:
                    self.gridCoords['authentications'] += [coord]


class Application(wx.App):
    def OnInit(self):
        super().OnInit()
        app = Helper(None)
        return app.Show(True)


if __name__ == '__main__':
    mainApp = Application()
    mainApp.MainLoop()
