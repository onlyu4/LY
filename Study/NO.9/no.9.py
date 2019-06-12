import requests
import time
from multiprocessing import Process,Queue
from  threading import Thread,Lock
# urls = ["http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%89%8B%E6%9E%AA%E5%9B%BE%E7%89%87&step_word=&hs=2&pn=1&spn=0&di=51150&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1029540617%2C752189348&os=2442465306%2C1791375783&simid=4164604806%2C686815948&adpicid=0&lpn=0&ln=447&fr=&fmq=1559361086115_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fs9.rr.itc.cn%2Fr%2FwapChange%2F20163_17_6%2Fa9rsul8672408620362.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F4_z%26e3Bf5i7_z%26e3Bv54AzdH3FgAzdH3Fnl9n890c0AzdH3F%23r&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
#         "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%89%8B%E6%9E%AA%E5%9B%BE%E7%89%87&step_word=&hs=2&pn=2&spn=0&di=880&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2937183941%2C1516391828&os=2146692826%2C2889853773&simid=0%2C0&adpicid=0&lpn=0&ln=447&fr=&fmq=1559361086115_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2F03.imgmini.eastday.com%2Fmobile%2F20180314%2F97a1c4ea4f6e5fbea3bf9626b9c3b930.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Ffr56pf_z%26e3Bjwfp1wy_z%26e3Bv54AzdH3FwAzdH3F8ban898ca88d9cdaaaaaa_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"]
#
# def func(url,i):
#     ret = requests.get(url)
#     tt = ret.content
#     with open(f"手枪{i}.jpg" ,"wb") as f:
#         f.write(tt)
#
# if __name__ == "__main":
#     p_list = []
#     for i,url in enumerate(urls):
#         p = Process(target=func, args=(url, i + 1))
#         p.start()

# def f1(n):
#     print(11111)
#     time.sleep(2)
#     print('>>>>>>',n)
#
# def f2(n):
#     print(22222)
#     time.sleep(3)
#     print('!!!!!!',n)
#
# if __name__ == '__main__':
#     #同步(串行)和异步  提交任务的方式
#     #f1()
#     #f2()
#     #阻塞和非阻塞  任务的执行状态
#     #进程的三状态 :就绪  运行  阻塞
#
#     #
#     p1 = Process(target=f1,args=(1,))
#     p2 = Process(target=f2,args=(2,))
#     #设置守护进行,必须start之前
#     p2.daemon = True
#     p1.start()
#     p2.start()
#     time.sleep(1)
#     print('主进程结束')

# def func(q):
#     ret = q.get()
#     print(f"子进程{ret}")
#
# if __name__ == '__main__':
#     q = Queue(3)
#     q.put("hi")
#     p = Process(target=func,args=(q,))
#     p.start()

#多线程

# def func():
#     print("111")
#
# if __name__ == '__main__':
#     p1 = Thread(target=func)
#     p2 = Thread(target=func)
#     p1.start()
#     p2.start()

n = 100

def f1(loc):
    with loc:
        # loc.acquire()  #加锁
        global n
        num = n
        num -= 1
        time.sleep(0.001)
        n = num
        # loc.release() #释放锁
if __name__ == '__main__':
    loc = Lock()
    t_list = []
    for i in range(10):
        t = Thread(target=f1,args=(loc,))
        t.start()
        # t.join()
        t_list.append(t)
    [tt.join() for tt in t_list]
    print(n)