
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？

import time

#1. 写装饰器器. 控制函数被调⽤用的频率. 要求: 5秒钟执⾏行行⼀一次. 少于5秒钟直接打印警告信息.
#
# start = 0
#
# def decorate_time(fn):
#     def inner(*args,**kwargs):
#         #把start引进来修改值
#         global start
#         #拿到当前的系统时间
#         stop_time = time.time()
#         #如果 当前系统时间减去调用的时间小于5
#         if stop_time - start > 5:
#             ret = fn(*args,**kwargs)
#             #重新赋予start的时间
#             start = time.time()
#             return ret
#         else:
#             print("调用的太快了。。。。")
#     return inner
#
# @decorate_time
# def target():
#     print("你好啊")
#
# target()
# time.sleep(6)
# target()

# 写装饰器器. 通过⼀一次调⽤用使函数执⾏行行5次
#
# def decorate(fn):
#     def inner(*args,**kwargs):
#         count = 0
#         while count < 5:
#             ret = fn(*args,**kwargs)
#             count+=1
#         return ret
#     return inner
#
# @decorate
# def target():
#     print("111")
# target()


#写装饰器器, 要求. 被装饰的函数在执⾏行行的时候⾸首先要判断登录状态. 如果是已经登录状态. 则直接执⾏行行. 否则提示⽤用户去执⾏行行登录操作. 直到⽤用户登录成功为⽌止

state = False
def decorate(fn):
    def inner(*args,**kwargs):
        global state
        name = "zhangsan"
        passwd = "123456"
        if state == False:
            uname = input("请登录\n请输入账号：")
            pwd = input("请输入密码：")
            if uname == name and passwd ==pwd:
                state = True
                ret = fn(*args,**kwargs)
                return ret
        else:
            ret = fn(*args, **kwargs)
            return ret
    return inner


@decorate
def target():
    print("欢迎登陆")
@decorate
def second_target():
    print("你已经登陆过了")

target()
target()
target()
