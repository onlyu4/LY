
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
#装饰器：
    #在不改变源代码和调用方式的情况下增加新的功能
    #

import time
def time_test(fn):
    def inner():
        start_time = time.time()
        fn()    #执行被装饰函数
        stop_time = time.time()
        print(f"函数的执行时间是::{stop_time-start_time}")
    return inner  #返回inner的内存地址
@time_test  #调用装饰器的代码
def add():
    print("你好啊，我是新增的函数")
#add()
a = False
def login(fn):
    def inner():
        global a
        if a:
            fn()
        else:
            user = "zhangsan"
            passwd = "123456"
            user_input = input("请输入你的账号：")
            passwd_input = input("请输入你的密码：")
            if user == user_input and passwd == passwd_input:
                a = True
                fn()
            else:
                print("账号或密码错误！")
    return inner


@login
def func():
    print("欢迎来到英雄联盟")


@login
def see():
    print("查看")
#func()
#see()

def wrapper(fn):
    def inner(*args,**kwargs):
        count = 0
        ret = None
        while count < 5:
            ret = fn(*args, **kwargs)
            count+=1
        return ret
    return inner

@wrapper
def func1():
    print("我是func1")
func1()