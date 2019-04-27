#编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码
def outer(fn):
    def inner():
        print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
        fn()
    return inner
@outer
def func():
    print("函数1")
func()
#编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
def external(fn):
    def inner():
        fn()
        print("每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码")
    return inner

@external
def func_1():
    print("函数2")
func_1()

#编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数
# def login(fn):
#     def inner():
#         count = 0
#         while count < 3:
#             user_name = input("请输入您的账号").strip()
#             user_passwd = input("请输入您的密码").strip()
#             if user_name == "admin" and str(user_passwd) == "123456":
#                 print("登陆成功")
#                 break
#             else:
#                 print("账号或密码错误，请从新输入。。。。")
#             count += 1
#             continue
#         fn()
#     return inner
#
# @login
# def func_2():
#     print("函数3")
# func_2()

#编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,
# 给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码.
import json
tag = False
def login_user():
    global tag
    with open("passwd.json","r",encoding="utf-8") as f:
        count = 0
        dic = json.load(f)
        for i in dic:
            while count < 3:
                name = input("name:")
                passwd = input("passwd:")
                if name == i and passwd == dic[i]:
                    print("login....")
                    tag = False
                    break
                else:
                    print("error....")
                    tag = False
                count += 1
                continue

def func_4(fn):
    def inner(*args,**kwargs):
        login_user()
        fn(*args,**kwargs)
    return inner
@func_4
def a():
    print("sadasd")
a()

