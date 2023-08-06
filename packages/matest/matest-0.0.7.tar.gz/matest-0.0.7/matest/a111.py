#一个遮盖背景颜色的图像做的桌面精灵
import wx
class myframe(wx.Frame):
    def __init__(self):
        self.x=100
        self.y=100
        super().__init__(parent=None,pos=(self.x,self.y),style=wx.FRAME_SHAPED|wx.STAY_ON_TOP)
        img=wx.Image("xin.bmp")
        #img.SetMaskColour(255, 242,0)
        #img.SetMaskFromImage(img,255, 242,0)
        #鼠标点击图片位置，可以打印特定位置坐标。
        #打印特定位置的点的红绿蓝三通道的颜色，方便设置遮罩
        posX=1
        posY=1
        print(img.GetRed(posX,posY),img.GetGreen(posX,posY),img.GetBlue(posX,posY))
        self.bg=wx.Bitmap(img)
        self.bg.SetMaskColour((255, 242,0))
        region=wx.Region(self.bg)
        self.SetShape(region)
        self.SetToolTip("皇天后土，主公在上")
        self.Bind(wx.EVT_PAINT,self.onPaint)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
    def OnLeftClickDown(self, event):
        pos = event.GetPosition()
        print(pos.x,pos.y)
        self.pt = wx.Point(pos.x,pos.y)
    def OnRightClickEvent(self, event):
        wx.Exit()
    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            self.Move((pos.x-self.pt.x,pos.y-self.pt.y))
    def onPaint(self,event):
        mydc=wx.PaintDC(self)
        mydc.DrawBitmap(self.bg,0,0,True)
myapp=wx.App()
frame=myframe()
frame.Show()
myapp.MainLoop()