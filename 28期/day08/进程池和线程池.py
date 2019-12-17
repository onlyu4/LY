
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

#进程池
from concurrent.futures import ProcessPoolExecutor
import time

def func(name):
    for i in range(10):
        time.sleep(1)
        print(name,i)

# if __name__ == '__main__':
#     p = ProcessPoolExecutor(5)  # 创建进程池（进程池中同时运行的进程数）
#     p.submit(func, "张三")
#     p.submit(func, "张三1")
#     p.submit(func, "张三2")
#     p.submit(func, "张三3")
#     p.submit(func, "张三4")
#     p.submit(func, "张三5")
#     p.submit(func, "张三6")
#     p.submit(func, "张三7")



#线程池

from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(10):
        print(name,i)
        time.sleep(1)

if __name__ == '__main__':
    t = ThreadPoolExecutor(3)
    t.submit(func, "wangwu1")
    t.submit(func, "wangwu2")
    t.submit(func, "wangwu3")
    t.submit(func, "wangwu4")
    t.submit(func, "wangwu5")
    t.submit(func, "wangwu6")
    t.submit(func, "wangwu7")