import os
import json

# filepath = os.path.dirname(os.getcwd()) + "/model/loginjson.json"
filepath  = "E:/PycharmProjects/Encapsulation/model/data/loginjson.json"
print(filepath)

filename = open(filepath, 'rb+')
result = json.load(filename)

# 使用for循环遍历数据，java序列化和反序列化
for name in result:
    print(name['logintabClass'])
    print(name['loginnameID'])
    print(name['nloginpwdID'])
    print(name['loginsubmitID'])
    print(name['username'])
    print(name['password'])
    print(name['msg'])
    print(name['expects'])


print(result)

