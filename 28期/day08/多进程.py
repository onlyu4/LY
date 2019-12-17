
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
from multiprocessing import Process
# def func1():
#     for i in range(1,10000):
#         print("func1",i)
#
def func2(name):
    for i in range(1,10000):
        print(name,i)

if __name__ == '__main__':
    p1 = Process(target=func2, args=(("lisi",)))
    p2 = Process(target=func2, args=("zhangsan",))
    p1.start()
    p2.start()

# class My_Process(Process):
#     def __init__(self, name):
#         super(My_Process,self).__init__()
#         self.name = name
#
#     def run(self):
#         for i in range(1,10000):
#             print(self.name, i)
#
# if __name__ == '__main__':
#     p1 = My_Process("func1")
#     p2 = My_Process("func2")
#     p1.start()
#     p2.start()