s = "淘金者"
print(s.encode("utf-8"))

#用什么编码方式进行编码，就用什么编码方式进行解码

bs = b'\xe6\xb7\x98\xe9\x87\x91\xe8\x80\x85'
print(bs.decode("utf-8"))


#字符串
s = "周的杰阿里里伦巴巴的呵呵"  #  把周杰伦 拼接成一个新的字符串并打印
print(s[0],s[2],s[6])
s = ("%s%s%s"%(s[0],s[2],s[6]))
print(type(s),s)
s.replace("原有的","要替换的")  #替换字符串
s.startswith("")    #判断字符串开头的字符   是的话返回True  不是的话返回False
s.endswith("")      #判断字符串开头的字符 是的话返回True 不是的话返回False
s.upper()       #将字符串全转换成大写
s.lstrip()      #将字符串全转换成小写
s.strip()       #删除字符串首尾字符，默认为空格
s.lstrip()      #删除字符串左面的字符
s.rstrip()      #删除字符串右面的字符
s.split()       #分割字符串
s.count("")     #统计符出出现的次数
s.capitalize()  #首字母大写
s.index("")     #查找字符串索引位置,没有的话会报错
s.find("")      #查找字符串索引的位置。没有的话返回-1
print(len(s))   #统计长度


#字符串切片
#语法：字符串[start;end:步长] 顾头不顾尾   步长控制切片的方向，正数从左到右，负数从右到左
s = "Java,Python,Php,C++"
print(s[5:11])

s1 = "123456789"
print(s1[::2])
print(s1[-2::-2])
information = "aNxYV"
infor = input("请输入验证码%s"%information)
if infor.upper() == information.upper():
    print("登陆成功")
else:
    print("验证码错误")


#for 循环
s = "dgfjkwej"
for i in s:
    print(i)

#列表

list = ["zhangsan","lisi","wangwu"]
list.append("wangermazi")   #再列表后追加元素
list.insert(0,"sunliu")     #在列表中插入一个元素，原有位置的元素向后推一位
list.extend(["张三","李四"])    #合并列表
#删除
list.pop(2)  #删除指定位置的元素
list.remove("李四")   #删除与之匹配的元素
list.clear()    #清空列表
print(list)

infor = input("请输入一个加法运算：")
infor = infor.split("+")
count = 0
for i in infor:
     count += int(i)
print(count)