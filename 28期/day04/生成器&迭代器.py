
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
#迭代器：
    #作用：让一个可迭代对象可以从里面拿到所有数据
        #在python中，中有可迭代对象才能拿到迭代器
        #迭代器一定是可迭代对象，可迭代对象不一定是迭代器

# list = ["张三","李四","王五"]
# it = list.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#
#
# def func():
#     print(123)
#     yield 456
#     print(789)
#     yield 000
#
# # ret = func()
# a = ret.__next__()
# # print(a)

# def func1():
#     list = []
#     for i in range(1000000):
#         list.append(f"数据{i}")
#         if i % 10 == 0:
#             yield list
#             list = []
#     yield list
#
#
# ret = func1()
# for i in ret:
#     print(i)

#list = [f"python{i}期"for i in range(1,29)]

# print(list)
# list = [i ** 2 for i in range(101) if i % 3 == 0]
# print(list)
#
# fn = lambda a,b,c : a + b + c
# ret = fn(1,2,3)
# print(ret)
lst = ["斯琴格日乐", "斯琴高娃", "斯大林", "斯坦达麦尔", "斯皮尔伯格"]
# def func(n):
#     return len(n)
#s = sorted(lst,key=lambda name:len(name))
#print(s)

name = filter(lambda n: n.startswitch("斯"), lst)
n = name(lst)
print(n)