# -*- coding: utf-8 -*-

import threading
from time import sleep
import sys

import wx

from YinerSpider import YinerSpider


class WorkThread(threading.Thread):
    def __init__(self,window,r,waittime):
        threading.Thread.__init__(self)
        self.window=window
        self.timeToQuit=threading.Event()
        self.timeToQuit.set()
        self.r=r
        self.count=1
        try:
            self.waittime=int(waittime)
        except:
            self.waittime=1

    def stop(self):
        if self.timeToQuit.isSet():
            self.timeToQuit.clear()
            msg=1
        else:
            msg=0
            self.timeToQuit.set()
        wx.CallAfter(self.window.ChangLabel, msg)

    def run(self):
        while 1:
            sleep(self.waittime)
            self.timeToQuit.wait()
            if self.r.data:
                rq=self.r.post()
            else:
                rq=self.r.get()
            if self.window.out:
                with open('out.txt','wb') as f:
                    sys.stdout=f
                    print rq.content,
            wx.CallAfter(self.window.LogMessage, self.count)
            self.count+=1

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 554,430 ), style =wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
        self.out=False

        self.SetSizeHintsSz( wx.Size( 537,430 ), wx.Size( 537,430 ) )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

        gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button13 = wx.Button( self.m_panel5, wx.ID_ANY, u"载入方案", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_button13, 0, wx.ALL, 5 )

        self.m_button14 = wx.Button( self.m_panel5, wx.ID_ANY, u"保存新方案", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_button14, 0, wx.ALL, 5 )

        self.URL = wx.StaticText( self.m_panel5, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.URL.Wrap( -1 )
        fgSizer3.Add( self.URL, 0, wx.ALL, 5 )

        self.m_textCtrl24 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        fgSizer3.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"DATA", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.m_textCtrl17 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), wx.TE_MULTILINE )
        fgSizer3.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"HEADERS", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.m_textCtrl18 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), wx.TE_MULTILINE )
        fgSizer3.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"频率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        fgSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )

        self.m_textCtrl20 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

        self.m_checkBox3 = wx.CheckBox( self.m_panel5, wx.ID_ANY, u"输出到文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_checkBox3, 0, wx.ALL, 5 )


        fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self.m_panel5, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_button3, 0, wx.ALL, 5 )

        self.m_button4 = wx.Button( self.m_panel5, wx.ID_ANY, u"暂停", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_button4, 0, wx.ALL, 5 )


        gSizer7.Add( fgSizer3, 1, wx.EXPAND|wx.LEFT|wx.TOP, 5 )


        gSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl22 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_MULTILINE )
        bSizer5.Add( self.m_textCtrl22, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


        gSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )


        self.m_panel5.SetSizer( gSizer6 )
        self.m_panel5.Layout()
        gSizer6.Fit( self.m_panel5 )
        bSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button13.Bind( wx.EVT_BUTTON, self.Open )
        self.m_button14.Bind( wx.EVT_BUTTON, self.Save )
        self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.Outfile )
        self.m_button3.Bind( wx.EVT_BUTTON, self.Start )
        self.m_button4.Bind( wx.EVT_BUTTON, self.Stop )

    def __del__( self ):
        pass

    def GetValue(self):
        if 'http://' in self.m_textCtrl24.GetValue():
            self.url=self.m_textCtrl24.GetValue()
        else:
            self.url='http://'+self.m_textCtrl24.GetValue()
        self.data=self.m_textCtrl17.GetValue()
        self.headers=self.m_textCtrl18.GetValue()
        self.waittime=self.m_textCtrl20.GetValue()

    def SetValue(self):
        self.m_textCtrl24.SetValue(self.url)
        self.m_textCtrl17.SetValue(self.data)
        self.m_textCtrl18.SetValue(self.headers)
        self.m_textCtrl20.SetValue(self.waittime)

    def ChangLabel(self,msg):
        if msg==1:
            self.m_button4.Label=u'继续'
        else:
            self.m_button4.Label=u'暂停'

    def Open( self, event ):
        dlg = wx.FileDialog(parent=None,message=u'选择新方案', style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.FileName = dlg.GetPath()
            dlg.Destroy()
            with open(self.FileName,'rb') as f:
                dict=eval(f.read())

            self.url=dict['url']
            self.data=dict['data']
            self.headers=dict['headers']
            self.waittime=dict['waittime']
            self.SetValue()

    def Save( self, event ):
        self.GetValue()
        dict={'url':self.url,'data':self.data,'headers':self.headers,'waittime':self.waittime}
        dlg = wx.FileDialog(parent=None,message=u'保存文件', style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.FileName = dlg.GetPath()
            dlg.Destroy()
            with open(self.FileName,'wb') as f:
                f.write(str(dict))

    def Outfile( self, event ):
        if self.out:
            self.out=False
        else:
            self.out=True

    def Start( self, event ):
        self.msg=''
        self.GetValue()
        r=YinerSpider(self.url)
        r.setheaders(self.headers)
        r.setdata(self.data)
        #print self.url,self.data,self.headers,self.waittime
        self.thread = WorkThread(self,r,self.waittime)
        self.thread.start()

    def Stop( self, event ):
        self.thread.stop()

    def LogMessage(self,count):
        self.msg+=u'第%d次执行成功！\n'%count
        self.m_textCtrl22.SetValue(self.msg)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame2(parent=None)
    frame.Show()
    app.MainLoop()
