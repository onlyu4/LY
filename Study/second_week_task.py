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
print(name.replace("l","p"))

#将name变量对应的值中的第一个"l"替换成"p",并输出结果
print(name.replace("l","p",1))

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
content = input("请输入内容:")
inform = content.split("+")
count = 0
for i in inform:
    count = count + int(i)
print(count)

实现一个整数加法计算器
content = input("请输入内容:")
inform = content.split("+")
count = 0
for i in inform:
    count = count + int(i)
print(count)

#计算用户输入的内容中有几个整数（以个位数为单位）
content = input("请输入内容:")
print(len(content))

#写代码，完成下列需求：
while True:
    input_user = input("请输入你选择回家了方式：").upper().strip()
    if input_user == "A":
        print("走大路回家")
        secone_input = input("选择公交车还是步行？").strip()
        if secone_input == "公交车":
            print("十分钟到家")
            break
        else:
            print("20分钟到家")
            break
    elif input_user == "B":
        print("走小路回家")
        break
    elif input_user == "C":
        print("显示绕道回家")
        thrid_input = input("是选择游戏厅玩会，还是网吧？").strip()
        if thrid_input == "游戏厅":
            print("一个半小时到家，爸爸在家，拿棍等你。")
            continue
        else:
            print("两个小时到家，妈妈已做好了战斗准备。")
            continue

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
name = input("请输入你的名字：")
place = input("请输入地点：")
hobby = input("请输入你的爱好")
print("敬爱可亲的%s，最喜欢在%s地%s"%(name,place,hobby))

#等待户输内容，检测户输内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输”，并允许户重新输并打印。敏感字符：“粉嫩”、“铁锤”
list_illegal  = ["粉嫩","铁锤"]
user_input = input("请输入")
if user_input in list_illegal:
    print("存在敏感字符，请重新输入")
else:
    print(user_input)

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
print(lis[3][2][1][0].upper())

#将列表中的数字3变成字符串"100"（用两种方式）
lis[1] = 100
lis[3][2][1][1] = 100

#利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
import json
li_1 = ["alex", "eric", "rain"]
a = "_".join(li_1)
print(a)

#利用for循环和range打印出下面列表的索引
li_2 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(len(li_2)):
    print(i)

#利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中
li_3 = []
for i in range(0,100,2):
    li_3.append(i)
print(li_3)

#利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中
li_4 = []
for i in range(50):
    if i%3 == 0:
        li_4.append(i)
print(li_4)

#利用for循环和range从100~1，倒序打印
for i in range(100,0,-1):
    print(i)

#利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来
li_5 = []
for i in range(100,9,-2):
    if i%4 ==0:
        li_5.append(i)
    print(i)
print(li_5)

#利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*
li = []
l2 = []
for i in range(1,31):
    li.append(i)
for n in li:
    if n % 3 == 0:
        n = "*"
    l2.append(n)
print(l2)

#查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表
li_7 = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
l3 = []
l4 = []
for i in li_7:
    l3.append(i.strip())
for i in l3:
    if (i.startswith("A") or i.startswith("a")) and i.endswith("c"):
        l4.append(i)
print(l4)

#开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符
li_8 = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
l5 = []
user_input = input("请输入内容：")
for i in li_8:
    if i in user_input:
        user_input = user_input.replace(i,"*"*len(i))
l5.append(user_input)
print(l5)

#有如下变量（tu是个元祖），请实现要求的功能
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

#a. 讲述元祖的特性
    #元组是不可变列表，只读列表，通常存放一些不不进行修改的数据
    #元组用（）来表示，空元组必须用tuple()来创建

#b. 请问tu变量中的第一个元素 "alex" 是否可被修改？
#不可以

#请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
#对应的列表，可以修改
tu[1][2]["k2"].append("Seven")
print(tu)

#请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
#对应的是元组，不可以修改

#字典dic
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

#请循环输出所有的key
for i in dic:
    print(i)

#请循环输出所有的value
for i in dic:
    print(dic[i])

#请循环输出所有的key和value
for i in dic:
    print(i,dic[i])

#请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic.setdefault("k4","v4")
print(dic)

#请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic["k1"] = "alex"
print(dic)

#请在k3对应的值中追加一个元素 44，输出修改后的字典
dic["k3"].append("44")
print(dic)

#请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(0,18)
print(dic)

av_catalog = {"欧美":{"www.youporn.com": ["很多免费的,世界最大的","质量一般"],
                    "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
                    "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
                    "x‐art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]},
              "日韩":{"tokyo‐hot":["质量怎样不清楚,个人已经不喜欢日韩范了",
                                 "verygood"]},
              "大陆":{"1024":["全部免费,真好,好人一生平安",
                            "服务器在国外,慢"]}}
#给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'
av_catalog["欧美"]["www.youporn.com"].insert(1,"量很大")
print(av_catalog)

#将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除
av_catalog["欧美"]["x‐art.com"].remove("全部收费,屌丝请绕过")
print(av_catalog)

#将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写
av_catalog["日韩"]["tokyo‐hot"][1]=av_catalog["日韩"]["tokyo‐hot"][1].upper()
print(av_catalog)

#给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
av_catalog["大陆"].setdefault("1048","['一天就封了'")
print(av_catalog)

#删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对
av_catalog["欧美"].pop("letmedothistoyou.com")
print(av_catalog)

#给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
av_catalog["大陆"]["1024"][0] = "可以爬下来,全部免费,真好,好人一生平安"
print(av_catalog)

#有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
st = "k:1|k1:2|k2:3|k3:4"
st_1 = st.split("|")
dic_1 = {}
for i in st_1:
    i1 = i.split(":")
    dic_1[i1[0]] = i1[1]
print(dic_1)

#有如下值将所有大于 66 的值保存至字典的第一个key中，将小于66 的值保存至第二个key的值中
lis_1= [11,22,33,44,55,66,77,88,99,90]
dic_2 = {"key1":[],"key2":[]}
for i in lis_1:
    if i > 66:
        dic_2["key1"].append(i)
    else:
        dic_2["key2"].append(i)
print(dic_2)
