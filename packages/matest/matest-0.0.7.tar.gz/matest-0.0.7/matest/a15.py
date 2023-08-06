import sys
import datetime

import wx
import wx.aui as aui
import wx.propgrid as wxpg
import wx.html2 as h2


AB = 'about:blank'

class AUIFrame(wx.Frame):

    def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.SetIcon(wx.Icon(name='app.ico', type=wx.BITMAP_TYPE_ICO))

        # tell FrameManager to manage this frame
        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        
        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        mb.Append(file_menu, "File")
        file_menu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        
        self.doEvt = wx.NewIdRef()
        file_menu.Append(self.doEvt, "操作")
        self.Bind(wx.EVT_MENU, self.OnDoEvt, id=self.doEvt)
        

        self.SetMenuBar(mb)
        
        self.statusbar = self.CreateStatusBar(2, wx.STB_SIZEGRIP)
        self.statusbar.SetStatusWidths([235, -1])
        self.statusbar.SetStatusText("Ready", 0)
        self.statusbar.SetStatusText("Welcome To wxPython!", 1)

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("tree").Caption("导航").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(False))

        self._mgr.AddPane(self.CreateHtmlCtrl(), aui.AuiPaneInfo().
                          Name("main").Center().CaptionVisible(False))

        self._mgr.AddPane(self.CreatePgCtrl(), aui.AuiPaneInfo().
                          Name("property").Caption("变量").Right().CaptionVisible(True))

        self._mgr.AddPane(self.CreateLogCtrl(), aui.AuiPaneInfo().
                          Name("log").Caption("日志").
                          Bottom().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
        # "commit" all changes made to FrameManager
        self._mgr.Update()

    def CreateTreeCtrl(self):
        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(240, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        root = tree.AddRoot("AUI Project")
        return tree

    def CreateLogCtrl(self):
        self.log = wx.TextCtrl(self,-1, '', wx.Point(0, 0), wx.Size(150, 90),
                               wx.NO_BORDER | wx.TE_MULTILINE)
        return self.log
    
    def CreatePgCtrl(self):
        self.pg = pg = wxpg.PropertyGridManager(self, size=wx.Size(240, 90),
                        style=wxpg.PG_SPLITTER_AUTO_CENTER |
                              wxpg.PG_AUTO_SORT | wxpg.PG_TOOLBAR)
        pg.AddPage( "Page 1 - Testing All" )

        pg.Append( wxpg.PropertyCategory("1 - Basic Properties") )
        pg.Append( wxpg.StringProperty("String",value="Some Text") )
        sp = pg.Append( wxpg.StringProperty('StringProperty_as_Password', value='ABadPassword') )
        # sp.SetAttribute('Hint', 'This is a hint')
        sp.SetAttribute('Password', True)
        
        pg.Append( wxpg.IntProperty("Int", value=100) )
        self.fprop = pg.Append( wxpg.FloatProperty("Float", value=123.456) )
        pg.Append( wxpg.BoolProperty("Bool", value=True) )
        boolprop = pg.Append( wxpg.BoolProperty("Bool_with_Checkbox", value=True) )
        pg.SetPropertyAttribute(
            "Bool_with_Checkbox",    # You can find the property by name,
            #boolprop,               # or give the property object itself.
            "UseCheckbox", True)     # The attribute name and value

        pg.Append( wxpg.PropertyCategory("2 - More Properties") )
        pg.Append( wxpg.LongStringProperty("LongString",
            value="This is a\nmulti-line string\nwith\ttabs\nmixed\tin."))
        pg.Append( wxpg.FileProperty("File",value=r"C:\Windows\system.ini") )
        pg.Append( wxpg.ArrayStringProperty("ArrayString",value=['A','B','C']) )

        pg.Append( wxpg.EnumProperty("Enum","Enum",
                                     ['wxPython Rules',
                                      'wxPython Rocks',
                                      'wxPython Is The Best'],
                                     [10,11,12],
                                     0) )
        pg.Append( wxpg.EditEnumProperty("EditEnum","EditEnumProperty",
                                         ['A','B','C'],
                                         [0,1,2],
                                         "Text Not in List") )

        pg.Append( wxpg.PropertyCategory("3 - Advanced Properties") )
        pg.Append( wxpg.DateProperty("Date",value=wx.DateTime.Now()) )
        pg.Append( wxpg.MultiChoiceProperty("MultiChoice",
                    choices=['wxWidgets','QT','GTK+']) )
        pg.AddPage( "第2页 啥也没有" )
        pg.Append(wxpg.StringProperty("Key", value="Value") )
            
        return pg
    
    def write(self, value):
        self.log.AppendText(value)

    def CreateHtmlCtrl(self):
        self.browser = browser = h2.WebView.New(self, style=wx.NO_BORDER)
        browser.LoadURL('file:///E:/Python/wx/a11.html')
        self.Bind(h2.EVT_WEBVIEW_NAVIGATED, self.OnWebViewNavigated, browser)
        self.Bind(h2.EVT_WEBVIEW_TITLE_CHANGED, self.OnWebviewTitleChanged, browser)
        self.Bind(h2.EVT_WEBVIEW_LOADED, self.OnWebviewLoaded, browser)
        return self.browser

    def OnExit(self, event):
        self.Close()

    def OnDoEvt(self, event):
        d = datetime.datetime.today()
        print(f"{d:%Y-%m-%d %H:%M:%S}: ", file=self)

    def OnWebViewNavigated(self, evt):
        if (url := evt.GetURL()) == AB:
            return 0
        print('OnWebViewNavigated:%s' % url, file=self)
        if '#' not in url:
            return 0
        cmd = url.split('#')[1]
        print(f'cmd={cmd}')
        if cmd == '1':
            # print([a for a in dir(evt)])
            print('EventType:%s' % evt.EventType, file=self)
            print('GetClassName:%s' % evt.GetClassName(), file=self)
            # print('SetEventObject:%s' % evt.SetEventObject())
        elif cmd == '2':
            print('SelectedText:【%s】' % self.browser.SelectedText, file=self)
        else:
            print(self.browser.PageSource)
        """
        ['GetClassInfo', 'GetClassName', 'GetClientData', 'GetClientObject', 'GetEventCa
          tegory', 'GetEventObject', 'GetEventType', 'GetExtraLong', 'GetId', 'GetInt', 'G
          etNavigationAction', 'GetRefData', 'GetSelection', 'GetSkipped', 'GetString', 'G
          etTarget', 'GetTimestamp', 'GetURL']
        """

    def OnWebviewTitleChanged(self, evt):
        """['EVT_WEBVIEW_ERROR', 'EVT_WEBVIEW_LOADED', 'EVT_WEBVIEW_NAVIGATED', 'EVT_WEBVIE
             W_NAVIGATING', 'EVT_WEBVIEW_NEWWINDOW', 'EVT_WEBVIEW_TITLE_CHANGED']
        """
        if (title := evt.GetString()) == AB:
            return 0
        print('OnWebviewTitleChanged:%s' % title, file=self)

    def OnWebviewLoaded(self, evt):
        if (url:=evt.GetURL()) == 'about:blank':
            return
        print(f'载入完成！{url=}', file=self)
        # print(browser.PageSource)
        # document.getElementById("msg");
        print('JS完成！', file=self)
        self.Bind(h2.EVT_WEBVIEW_LOADED, None, self.browser)


if __name__ == '__main__':
    app = wx.App()
    frame = AUIFrame(None, wx.ID_ANY, "测试伴侣AUI", size=(1280, 720))
    frame.Show()
    app.MainLoop()
