
import unittest
from unit import loginaccount,jdlogin,shop
import HTMLTestRunner
import os



suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(loginaccount.LoginAccount))
# suit.addTest(unittest.makeSuite(jdlogin.Login))
# suit.addTest(unittest.makeSuite(shop.Shop))

# filename = os.getcwd() + "/HTML/jd.html"
filename = "E:/PycharmProjects/Encapsulation/HTML/jd_shop.html"
# 指定二进制的编码格式，rb:只读；wb：只写；rb+:可读可写
files = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=files,
    title=u"京东",
    description=u"京东测试报告"
)

runner.run(suit)