import test
# import sys
# print(sys.path)
# print(test.name)
# print(test.func())
# print(test.__name__)


#type 判断是什么数据类型

# name = "呵呵"
# print(type(name))
#
# nub = 222
# print(type(nub))
#
# def func():
#     pass
# print(type(func))
#
# #isinstance()   判断xxx是否为xxx类型
#
# print(isinstance(name,str))
#
# #issubclass()   判断xxx是否为xxx的子类
#
# class animal():
#     pass
#
# class dog(animal):
#     pass
#
# print(issubclass(dog,animal))

# while 1:
#     user_input = input(">>>>>>:")
#     if hasattr(test,user_input):
#         fn = getattr(test,user_input)
#         if callable(fn):
#             fn()
#         else:
#             print(fn)
#     else:
#         print("error.....")

#约束

# class foo():
#     def login(self):
#         raise NotImplementedError("没有重写")
#
# class admin(foo):
#     def login(self):
#         print("登陆成功")
# a = admin()
# a.login()

#第二种方法

from abc import ABCMeta,abstractmethod

class foo(metaclass=ABCMeta):
    @abstractmethod
    def login(self):
        pass

class admin(foo):
    def login(self):
        print("登陆成功")

p = admin()
p.login()