# Author:Scott She

import getpass

_username = "scott"
_password = "666666"

username = input("username ")

# 注意, 该方法在PyCharm中不能运行,可以用命令行测试
password = getpass.getpass("password ")


if _username == username and _password == password:
    print("Wellcom {name} login...".format(name=username))
else:
    print("Invalid username or password!")

