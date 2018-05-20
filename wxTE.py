import wx

class Window(wx.Frame):
 
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (300,250))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)
 
        menu = wx.Menu()
        openItem = menu.Append(wx.ID_OPEN, "Open", "Push the button to open the file")
        aboutItem = menu.Append(wx.ID_ABOUT,"About","Push the button to get an information about this application")
        exitItem = menu.Append(wx.ID_EXIT,"Exit","Push the button to leave this application")
        bar = wx.MenuBar()
        bar.Append(menu,"File")
        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
 
    def OnOpen(self, e):
        self.dirname = " "
        openDlg = wx.FileDialog(self, "Choose a file to open", self.dirname, " ", "*.*")
        if openDlg.ShowModal() == wx.ID_OK:
                self.filename = openDlg.GetFilename()
                self.dirname = openDlg.GetDirectory()
                f = open(os.path.join(self.dirname,self.filename), "r")
                self.control.SetValue(f.read())
                f.close()
                wnd.SetTitle(self.filename + " - pyNote")
 
    def OnAbout(self, e):
        aboutDlg = wx.MessageDialog(self, "This is a mini editor keeping your text","About pyNote", wx.OK)
        aboutDlg.ShowModal()
        
    def OnExit(self, e):
        self.control.SetValue("Close me, please! :(")
 
app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()