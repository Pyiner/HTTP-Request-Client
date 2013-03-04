__author__ = 'Yiner'
#coding=utf-8
import requests

class YinerSpider():
    def __init__(self,url):
        self.url=url
        self.headers={}
        self.data={}
        self.cookies={}
        self.s=requests.session()

    def get(self):
        self.r=self.s.get(url=self.url,headers=self.headers)
        return self.r

    def post(self):
        self.r=self.s.post(url=self.url,headers=self.headers,data=self.data)
        return self.r

    def setheaders(self,headers):
        if isinstance(headers,dict):
            self.headers=headers
        else:
            self.headers=self.TextToDict(headers)


    def setdata(self,data):
        if isinstance(data,dict):
            self.data=data
        else:
            self.data=self.TextToDict(data)

    def changeurl(self,url):
        self.url=url

    def TextToDict(self,str):
        str="'"+str+"'"
        d='{'+str.replace('\n',"""',\n'""")+"}"
        hlist=[]
        tip=True
        j=0
        ans=0
        for i in d:
            if i ==':' and tip:
                hlist.append(d[j:ans])
                j=ans+1
                tip=False
            elif ans+1==len(d):
                hlist.append(d[j:])
            if i=='\n':
                tip=True
            ans+=1
        fstr=''
        for h in hlist:
            fstr+=h.strip()+"':'"
        try:
            dicta=eval(fstr.rstrip("':'"))
            if isinstance(dicta,dict)==False:
                dicta={}
        except:
            dicta={}
        return dicta

if __name__=='__main__':
    y=YinerSpider('http://passport.cnblogs.com/login.aspx?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F')
    y.setdata("""__EVENTTARGET:
__EVENTARGUMENT:
__VIEWSTATE:/wEPDwUL  LTE1MzYzODg2NzZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtjaGtSZW1lbWJlcm1QYDyKKI9af4b67Mzq2xFaL9Bt
__EVENTVALIDATION:/wEWBQLWwpqPDQLyj/OQAgK3jsrkBALR55GJDgKC3IeGDE1m7t2mGlasoP1Hd9hLaFoI2G05
tbUserName:ljy1992
tbPassword:162345
btnLogin:登  录
txtReturnUrl:http://www.cnblogs.com/""")#python 字符串引号的区别
    r=y.post()
    #print r.text
    #y.changeurl('http://www.cnblogs.com/cyiner/admin/EditPosts.aspx')
    #r=y.get()
    #print r.text