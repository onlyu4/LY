#字典
#key-value
info = {
    "001":"zhangsan",
    "002":"lisi",
    "003":"wangwu",
    "004":"sunliu",
}
'''
print(info["003"])  #查找，字典里面有这个值时，打印出值，没有时，会报错
print(info.get("007"))  #查找，字典里面有这个值时，打印出值，没有时，打印none。
info["001"] = "张三"  #修改键值
del info ["001"]  #删除
info.pop("003")  #删除
info.popitem()  #随机删除
#info.update(字典名)  #有相同的key值时，键值会被替换掉，没有时，会会创建新的key以及键值
'''
for i in info:
    print(i,info[i])  #循环字典

