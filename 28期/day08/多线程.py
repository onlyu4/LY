
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

from  threading import Thread,RLock

# def func(name):
#     for i in range(1,10000):
#         print(name, i)
#
# if __name__ == '__main__':
#     p1 = Thread(target=func, args=("线程1",))
#     p2 = Thread(target=func, args=("线程2",))
#     p1.start()
#     p2.start()
# n = 0
# def func(Lock:Lock):
#     global n
#     for i in range(1000000):
#         Lock.acquire()  # 上锁
#         n+=1
#         Lock.release()  # 解锁
#
# if __name__ == '__main__':
#     lock = Lock()
#     p1 = Thread(target=func, args=(lock,))
#     p2 = Thread(target=func, args=(lock,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(n)

n = 0
def func(Lock:RLock):
    global n
    for i in range(1000000):
        Lock.acquire()  # 上锁
        Lock.acquire()  # 上锁    死锁
        n+=1
        Lock.release()  # 解锁
        Lock.release()  # 解锁

if __name__ == '__main__':
    lock = RLock()
    p1 = Thread(target=func, args=(lock,))
    p2 = Thread(target=func, args=(lock,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(n)