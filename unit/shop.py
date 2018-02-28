import unittest
import time
from shopcart.shop_control import shopcontrol
from login.control import logincontrol

class Shop(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = shopcontrol.ShopControl()
        # self.login = logincontrol.LoginControl()
        pass

    def setUp(self):
        self.driver.start()
        self.driver.ShopClickLogin(u"登录")
        pass

    def tearDown(self):
        self.driver.close()
        pass

    def test_shop_cart(self):
        # 计算购物车总价
        self.driver.ShopCartCount(self)
        pass

# if __name__ == '__main__':
#     unittest.main()