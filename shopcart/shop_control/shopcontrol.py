from selenium import webdriver
from util import firefoxutil,urlutil
import time
from login.control import logincontrol

class ShopControl(object):
    def __init__(self):

        # 实例化浏览器
        self.firefox = firefoxutil.StartFirfox()

        #实例化登陆
        # self.login = logincontrol.LoginControl()

    def start(self):
        self.firefox.OpenFirefox(urlutil.URL.JD_SHOPCART)

    def close(self):
        self.firefox.CloseFirfox()

    # 点击登录按钮，进行登录
    def ShopClickLogin(self,linktext):
        self.firefox.ClickLinkText(linktext)

        # 开始切换frame控件
        self.firefox.SwitchFrame("dialogIframe")

        # 输入内容
        login_tab_r = self.firefox.FindClassname('login-tab-r').click()

        loginname = self.firefox.Findid('loginname').send_keys("18811358710")
        nloginpwd = self.firefox.Findid('nloginpwd').send_keys("fu910124")
        loginsubmit = self.firefox.Findid('loginsubmit').click()

    #计算购物车的价格同时作对比
    def ShopCartCount(self,self1):

        self.firefox.driver.switch_to_default_content()
        p_sums = self.firefox.FindClassnames("p-sum")
        sumPrice = self.firefox.FindClassname("sumPrice")

        p_list = []

        for temp in p_sums:
            temp_after = str(temp.text)[1:].split('\n')[0]
            p_list.append(float(temp_after))

        # 计算总价
        sums = 0
        for temp in p_list:
            sums += temp

        # 获取已优惠金额:-¥41.40  并截取
        totalRePrice = self.firefox.FindClassname("totalRePrice")
        totalRePrice_after = str((totalRePrice.text)[2:])

        # 断言
        # 对获取的内容进行编码
        # sprice = (sumPrice.text).encode('UTF-8')
        # sumPrice_after = str(sumPrice.text).replace("¥","")

        sumPrice_after = str(sumPrice.text)[1:]
        FinalSum = sums - float(totalRePrice_after)
        self1.assertEqual('{:.2f}'.format(FinalSum),'{:.2f}'.format(float(sumPrice_after)))


