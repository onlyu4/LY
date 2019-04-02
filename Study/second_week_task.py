#1、有变量name = "aleX leNb" 完成如下操作：
#1)  移除 name 变量对应的值两边的空格,并输出处理结果
name = "aleX leNb"
#print(name.strip())

#2)  移除name变量左边的"al"并输出处理结果
#print(name.replace("al",""))    #replace 替换字符串
print(name.lstrip("al"))

#移除name变量右面的"Nb",并输出处理结果
# print(name.replace("Nb",""))
print(name.rstrip("Nb"))

#移除name变量开头的a"与最后的"b",并输出处理结果
print(name.strip("ab"))  #strip  去掉首尾的字符

#判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith("al"))

#判断name变量是否以"Nb"结尾,并输出结果
print(name.endswith("Nb"))

#将 name 变量对应的值中的所有的"l" 替换为 "p",并输出结果
#print(name.replace("l","p"))

#将name变量对应的值中的第一个"l"替换成"p",并输出结果
#print(name.replace("l","p",1))

#将 name 变量对应的值根据所有的"l" 分割,并输出结果
print(name.split("l"))

#将name变量对应的值根据第一个"l"分割,并输出结果
print(name.split("l",1))

#将 name 变量对应的值变大写,并输出结果
print(name.upper())

#将 name 变量对应的值变小写,并输出结果
print(name.lower())

#将name变量对应的值首字母"a"大写,并输出结果
print(name.capitalize())

#判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count("l"))

#判断name变量对应的值前四位"l"出现几次,并输出结果
print(name.count("l",0,3))

#从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
print(name.index("N"))

#从name变量对应的值中找到"N"对应的索引(如果找不到则返回‐1)输出结果
print(name.find("N"))

#从name变量对应的值中找到"X le"对应的索引,并输出结果
print(name.index("X le"))

#请输出 name 变量对应的值的第 2 个字符
print(name[1])

#请输出 name 变量对应的值的前 3 个字符
print(name[0:3])

#请输出 name 变量对应的值的后 2 个字符
print(name[-2:])

#请输出 name 变量对应的值中 "e" 所在索引位置
print(name.find("e"))

s = "123a4b5c"
#通过对s切片形成新的字符串s1,s1 = "123"
s1 = s[0:3]
print(s1)

#通过对s切片形成新的字符串s2,s2 = "a4b"
s2 = s[3:6]
print(s2)

#通过对s切片形成新的字符串s3,s3 = "1345"
s3 = s[0::2]
print(s3)

#通过对s切片形成字符串s4,s4 = "2ab"
s4 = s[1:-1:2]
print(s4)

#通过对s切片形成字符串s5,s5 = "c"
s5 = s[-1]
print(s5)

#通过对s切片形成字符串s6,s6 = "ba2"
s6 = s[-3::-2]
print(s6)

#使用while或for循环分别打印字符串s="asdfer"中每个元素
s="asdfer"
for i in s:
    print(i)

#使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
for i in s:
    print(s)

#使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb，例如：asb, bsb，csb,...gsb
for i in s:
    print(i,"sb")

#使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"
x="321"
for i in x:
    print("倒计时%s秒"%i)
print("出发")

#实现一个整数加法计算器(两个数相加)
# content = input("请输入内容:")
# inform = content.split("+")
# count = 0
# for i in inform:
#     count = count + int(i)
# print(count)

#实现一个整数加法计算器
# content = input("请输入内容:")
# inform = content.split("+")
# count = 0
# for i in inform:
#     count = count + int(i)
# print(count)

#计算用户输入的内容中有几个整数（以个位数为单位）
# content = input("请输入内容:")
# print(len(content))

#写代码，完成下列需求：
# while True:
#     input_user = input("请输入你选择回家了方式：").upper().strip()
#     if input_user == "A":
#         print("走大路回家")
#         secone_input = input("选择公交车还是步行？").strip()
#         if secone_input == "公交车":
#             print("十分钟到家")
#             break
#         else:
#             print("20分钟到家")
#             break
#     elif input_user == "B":
#         print("走小路回家")
#         break
#     elif input_user == "C":
#         print("显示绕道回家")
#         thrid_input = input("是选择游戏厅玩会，还是网吧？").strip()
#         if thrid_input == "游戏厅":
#             print("一个半小时到家，爸爸在家，拿棍等你。")
#             continue
#         else:
#             print("两个小时到家，妈妈已做好了战斗准备。")
#             continue

#写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和
count = 0
for i in range(0,100):
    if i%2 != 0:
        count = i + count
    elif i == 88:
        continue
    else:
        count = count - i
print(count)

#制作趣味模板程序需求：等待户输名字、地点、爱好，根据户的名字和爱好进任意现实
# name = input("请输入你的名字：")
# place = input("请输入地点：")
# hobby = input("请输入你的爱好")
# print("敬爱可亲的%s，最喜欢在%s地%s"%(name,place,hobby))

#等待户输内容，检测户输内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输”，并允许户重新输并打印。敏感字符：“粉嫩”、“铁锤”
# list_illegal  = ["粉嫩","铁锤"]
# user_input = input("请输入")
# if user_input in list_illegal:
#     print("存在敏感字符，请重新输入")
# else:
#     print(user_input)

#写代码，有如下列表，按照要求实现每一个功能
li = ["alex", "WuSir", "ritian", "barry", "wenzhou","eric"]

#计算列表的长度并输出
print(len(li))

#列表中追加元素"seven",并输出添加后的列表
print(li.append("seven"),li)

#请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(0,"Tonny")
print(li)

#请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1] = "Kelly"
print(li)

#请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加
l2=[1,"a",3,4,"heart"]
li.extend(l2)
print(li)

#请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加
s = "qwert"
li.extend(s)
print(li)

#请删除列表中的元素"eric",并输出添加后的列表
li.remove("eric")
print(li)

#请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li.pop(1)
print(li)

#请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[1:5]
print(li)

#请将列表所有得元素反转，并输出反转后的列表
li.reverse()
print(li)

#请计算出"alex"元素在列表li中出现的次数，并输出该次数
print(li.count("alex"))

#写代码，有如下列表，利用切片实现每一个功能
list = [1, 3, 2, "a", 4, "b", 5,"c"]

#通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
list1 = list[0:3]
print(list1)

#通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
list2 = list[4:7]
print(list2)

#通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
list3 = list[0::2]
print(list3)

#通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
list4 = list[1:-2:2]
print(list4)

#通过对li列表的切片形成新的列表l5,l5 = ["c"]
list5 = list[7:]
print(list5)

#通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
list6 = list[-3::-2]
print(list6)

#写代码，有如下列表，按照要求实现每一个功能
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

#将列表lis中的"tt"变成大写（用两种方式）
#lis[3][0] = "TT"
lis[3][0][0].upper()
print(lis)
