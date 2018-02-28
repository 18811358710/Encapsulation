from util import firefoxutil,urlutil
import unittest
import time
from login.control import logincontrol

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # self.login = logincontrol.LoginControl()

        pass
    def setUp(self):
        self.login.start(urlutil.URL.JD_LOGIN)
        time.sleep(2)
        pass
    def tearDown(self):
        self.login.close()
        pass


    # def test_login1(self):
    #     U"""用户名、密码为空时，登陆失败，添加断言"""
    #
    #
    #     pass
    def test_login2(self):
        U"""用户名、密码输入正确，登陆成功，跳转首页"""

        self.login.LoginClick("18811358710","fu910124")
        self.login.LoginAssert(self,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
        pass