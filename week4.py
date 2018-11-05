#字典
'''
info = {
    "001" : "zhangsan",
    "002" : "lisi",
    "003" : "wangwu",
    "004" : "zhaoliu"
}

print(info["001"])  #查找，如果没有相对应的值会报错
info["001"] = "张三" #更改
info["005"] = "李四" #增加
#del #删除，内置的删除方式，不是字典和列表特定的删除方式。
del info["005"]
info.pop("001") #info.pop()删除对应的值
#info.popitem() #随机删除
print(info)
print(info.get("003")) #查找，没有相对应的值不会报错
print("001" in info) #判断字典中是否有相应的值，有的话返回True，没有的话返回False
print(info.keys()) #打印所有的key
print(info.values())  #打印所有的values

b = {
    "001" : "liuyan",
    "007" : "yangwei",

}
info.update(b) #upadte，合并两个字典，有相同的key，合并更新值，不同的key，添加值
print(info)
print(info.items())  #items将字典转成列表
for i in info:
    print(i,info[i])
                   #字典循环

#集合:
      #集合是一个无序的，不重复的数据结合，他的主要作用如下：
           #去重，把一个列表变成集合，自动去重。
           #关系测试，测试两组数据之前的交集，差集，并集等关系。
list_1 = set([1,2,3,8,9,6,54,3,4])
list_2 = set([1,2,3,4,5,6])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集
print(list_1.difference(list_2))

#子集
print(list_1.issubset(list_2))
print(list_2.issubset(list_1))

#求交集
print(list_1 & list_2)

#求并集
print(list_1 | list_2)

#求差集
print(list_1 - list_2)

#求对称差集
print(list_2 ^ list_1)

#添加
list_1.add(888)  #添加一个数值
print(list_1)
list_1.update([777,888,999,666])   #添加多个值
print(list_1)

#删除
list_1.remove()
print(list_1)
'''

'''
#文件操作
f = open('file_txt','a',encoding='utf-8')   #打开file_txt文件并读取，编码为utf-8  文件句柄  a:追加，在文件的后面添加 ，w写  r读
f.write('十年\n')
f.write('陈奕迅\n')
f.close()
'''

'''
f = open('file_txt','r',encoding='utf-8')
#print(f.readline())     #打印一行
#for i in range(5):
#    print(f.readline())     #打印前五行
for index,i in enumerate(f.readlines()):  #index打印列表下标，enumerate取出index打出的下标
    if index == 9 :
        print('------我是分割线---------')
        continue
    print(i.strip())  #打印全部，第九行替换成“------我是分割线”
'''
#打印第九行并替换成=================我是分割线====================
'''
f = open('file_txt','r',encoding='utf-8')
count = 0
for i in f:
    if count == 9:
        print('===================我是分割线=================')
    print(i)
    count += 1
f.close()
'''
'''
f = open('file_txt','r',encoding='utf-8')
#print(f.tell())   #打印文件句柄指针所在的位置
print(f.read(3))    #打印第三个字符
f.seek(5)   #回到第五个字符
print(f.tell())  #f.tell 查看在第几个位置
'''
'''
#读写
f = open('file_txt','r+',encoding='utf-8')  #r+，对文件进行读写，但是写只能写在文件的后面
for i in range(10):
    print(f.readline())
f.write('\n+++++++++++++++++')
'''

'''
#写读
f = open('file_txt','w+',encoding='utf-8')
for i in range(4):
    print(f.readline())
f.write("--------------ngw-------------\n")
f.write("--------------ngw-------------\n")
f.write("--------------ngw-------------\n")
f.seek(2)
f.write("+++++++++++++++++++++++++++++\n")
print(f.tell())
f.close()
'''

'''
#二进制读
f = open('file_txt','rb')
print(f.readline())
'''

'''
#二进制写
f = open("file_txt", 'wb')
(f.write('hello world\n'.encode()))
f.close()
'''

import sys,time
for i in range(30):
    sys.stdout.write('>>>>>>')
    sys.stdout.flush()
    time.sleep(0.1)
