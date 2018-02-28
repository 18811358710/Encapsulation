
import unittest

from login.control import logincontrol
from  util import urlutil
from model.control import loginjsoncontrol


class LoginAccount(unittest.TestCase):

    # 所有测试用例执行之前的方法
    @classmethod
    def setUpClass(self):
        self.login = logincontrol.LoginControl()

        self.jsoncontrol= loginjsoncontrol.LoginJsonControl()

        pass
    def setUp(self):
        self.login.start(urlutil.URL.JD_LOGIN)
        pass


    def tearDown(self):
        self.login.close()
        pass

    def test_user_model(self):
        for index in self.jsoncontrol.GetJsonList():
            self.login.LoginClick(index['logintabClass'],
                                  index['loginnameID'],
                                  index['nloginpwdID'],
                                  index['loginsubmitID'],
                                  index['username'],
                                  index['password'])
            # 断言
            self.login.LoginAssertMsg(self,index['msg'],index['expects'])

            self.login.Clear(index['loginnameID'],index['nloginpwdID'])











