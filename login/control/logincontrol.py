from util import firefoxutil
import time
from selenium import webdriver
import unittest


class LoginControl(object):
    def __init__(self):
        self.firefox = firefoxutil.StartFirfox()

    def start(self,url):
        self.firefox.OpenFirefox(url)

    def close(self):
        self.firefox.CloseFirfox()



    # def LoginClick(self,username,password):
    #     login_tab_r = self.firefox.FindClassname('login-tab-r').click()
    #
    #     loginname = self.firefox.Findid('loginname').send_keys(username)
    #     nloginpwd = self.firefox.Findid('nloginpwd').send_keys(password)
    #     loginsubmit = self.firefox.Findid('loginsubmit').click()

    def LoginClick(self,logintabClass,
                   loginnameID,
                   nloginpwdID,
                   loginsubmitID,
                   username,password):
        login_tab_r = self.firefox.FindClassname('login-tab-r').click()

        loginname = self.firefox.Findid('loginname').send_keys(username)
        nloginpwd = self.firefox.Findid('nloginpwd').send_keys(password)
        loginsubmit = self.firefox.Findid('loginsubmit').click()

    #对输入框清除
    def Clear(self,loginname,nloginpwd):
        self.firefox.Clear(loginname)
        self.firefox.Clear(nloginpwd)

    # 错误提示断言
    def LoginAssertMsg(self,self1,widget,expects):
        msg = self.firefox.FindClassname(widget).text
        self1.assertEqual(msg,expects)

    def LoginAssert(self,self1,excepts):
        title = self.firefox.GetTitle()
        self1.assertEqual(title,excepts)

    # 轮播图封装
    def MainBanner(self,self1,imgclass,circleclass,expects):
        circles = self.firefox.FindClassnames(circleclass)

        for index in range(1,len(circles)):
            self.firefox.ActionMove1(circles[index])
            # 获取控件同时进行断言
            lis = self.firefox.FindClassnames(imgclass)
            self1.assertEqual(lis[index].get_attribute("class"),expects)



