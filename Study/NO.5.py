#带参数的装饰器
# def wrapper_out(tag):
#     def wrapper(fn):
#         def inner(*args,**kwargs):
#             if tag:
#                 print("执行前")
#                 ret = fn(*args,**kwargs)
#                 print("执行后")
#                 return ret
#             else:
#                 ret = fn(*args,**kwargs)
#                 return ret
#         return inner
#     return wrapper
# @wrapper_out(True)
# def funce():
#     print("111111")
# funce()
# @wrapper_out(False)
# def func_2():
#     print("22222")
# func_2()

# def warpper(tag):
#     def log(fn):
#         def inner(*args, **kwargs):
#             if tag:
#                 ret = fn(*args, **kwargs)
#                 # 记录日志
#                 return ret
#         return inner

#统计列表中周杰伦出现的次数
# from collections import Counter
# lis  = ["周杰伦","周杰伦","李四"]
# count = Counter(lis)    #计数器 统计列表中每个元素出现的次数
# print(count.get("周杰伦"))
#
# #默认值字典
# from collections import defaultdict
# dic = defaultdict(lambda : 0)   #默认值
# print(dic["张三"])    #字典中没有“张三”这个key时会新增这个“key”
# print(dic)
# dic["张三"] = 100
# print(dic)
#
# #取随机数
# import random
# print(random.random())  #取0--1之间的小数     random取随机小数
# print(random.randint(1,100))    #取1--100之间的正数   randint取随机整数

#time
import time

#取当前时间戳
# time_time = time.time()
# print(time.time())
#
# #时间戳转换结构化时间
# struct_time = time.localtime(time_time)
# print(struct_time)
#
# #结构化时间转换格式化时间
# ftime = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
# print(ftime)
#
# #格式化时间转换结构化时间
# stime = time.strptime(ftime,"%Y-%m-%d %H:%M:%S")
# print(stime)
#
# #格式化时间转换成时间戳
# ttime = time.mktime(stime)
# print(ttime)

##求时间差
s1 = "1989-01-01 12:00:00"
s2 = "1989-01-02 14:35:00"

stime_1 = time.mktime(time.strptime(s1,"%Y-%m-%d %H:%M:%S"))
stime_2 = time.mktime(time.strptime(s2,"%Y-%m-%d %H:%M:%S"))
ttime = stime_2-stime_1


import pickle

#数据转化成字节
lis = ["张三","李四","王五"]
bs = pickle.dumps(lis)
print(bs)

#字节转化数据
print(pickle.loads(b'\x80\x03]q\x00(X\x06\x00\x00\x00\xe5\xbc\xa0\xe4\xb8\x89q\x01X\x06\x00\x00\x00\xe6\x9d\x8e\xe5\x9b\x9bq\x02X\x06\x00\x00\x00\xe7\x8e\x8b\xe4\xba\x94q\x03e.'))

#json
import json

#把字典转化成json串（字符串）
dic = {"张三":22,"李四":26,"王五":38}
s = json.dumps(dic,ensure_ascii=False)
print(s,type(s))

#将字符串转化成字典
a = '{"张三": 22, "李四": 26, "王五": 38}'
n = json.loads(a)
print(n,type(n))