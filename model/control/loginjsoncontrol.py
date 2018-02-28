import json
import os

class LoginJsonControl(object):
    # 解析json方法
    def __init__(self):
        # 指定json路径
        filepath = "E:/PycharmProjects/Encapsulation/model/data/loginjson.json"
        self.filename = open(filepath,encoding='utf-8')
        # self.result = json.load(self.filename)

        pass
    def GetJsonList(self):
        self.result = json.load(self.filename)
        # 返回list
        return self.result
    #
    # def GetAcount(self):
    #     return self.result


# json 文件、jsoncontrol类、单元测试类、单元测试控制类、url、基础控制类、suit测试组件