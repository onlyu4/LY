
list_2 = []
with open("a1.txt","r",encoding="utf-8") as f:
    list_1 = f.readline().strip().split(",")  #取表头并进行切片
    #print(list_1)
    for i in f:
        #print(i)
        list = i.strip().split(",")#取到之后的所有内容
        #print(list)
        dic = {}
        for i in range(len(list_1)):    #循环的次数是list_1的长度
            dic[list_1[i]] = list[i]    #定义字典的key和value
        list_2.append(dic)      #将字典添加到列表中
print(list_2)

#传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果
user_input = input("请输入：")
def count(user_input):
    number = 0
    letter = 0
    space = 0
    other = 0
    for i in user_input:
        if i.isdigit():  #isdigit判断是否为数字
            number += 1
        elif i.isalpha():   #isalpha判断是否为字母
            letter += 1
        elif i.isspace():   #isspace判断是否为空格
            space +=1
        else:
            other += 1
    print("字母的个数为:%s"%letter)
    print("数字的个数为:%s"%number)
    print("空格个数为:%s"%space)
    print("其他字符个数为:%s"%other)
count(user_input)

#写函数，接收两个数字参数，返回比较大的那个数字
def campare(a,b):
    if a > b:
        return a
    else:
        return b
#print(campare(1,2))

#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def func(arg):
    dic_new = {}
    for key,value in arg.items():
        if len(value) > 2:
            dic_new[key] = value[0:2]
        else:
            dic_new[key] = value
    print(dic_new)
#func(dic)

#写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。
# 例如传入的列表为：[11,22,33] 返回的字典为{0:11,1:22,2:33}
lis = [11,12,14,15,22,33,44]

def func_1(arg):
    dic_1 = {}
    for i in enumerate(arg):
        dic_1[i[0]] = i[1]
    return dic_1
#print(func_1(lis))

#写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容追加到一个student_msg文件中
def information(name,sex,age,education):
    with open("student_msg","a",encoding="utf-8") as f:
        f.write("姓名：%s\t性别：%s\t年龄：%s\t学历：%s\t"%(name,sex,age,education))
#information("刘岩","男",22,"本科")

#支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女
def information_second(name,age,education,sex="男"):
    with open("student_msg","a",encoding="utf-8") as f:
        f.write("姓名：%s\t性别：%s\t年龄：%s\t学历：%s\t" % (name, sex, age, education))
while True:
    user_input = input("按Q或者q退出")
    if user_input.upper() == "Q":
        break
    else:
        name = input("请输入您的名字")
        age = input("请输入您的年龄")
        education = input("请输入您的学历\n")
        sex = input("请输入您的性别")
    #information_second(name,age,education,sex)

#写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
import os
def file(name_file_old,file_content_old,file_content,name_file_new):
    with open(name_file_old, "r", encoding="utf-8") as f, open(name_file_new, "w", encoding="utf-8") as f2:
        for i in f:
            if file_content_old in i:
                i = i.replace(file_content_old,file_content)
                f2.write(i)
            else:
                f2.write(file_content)
    os.remove(name_file_old)
    os.mkdir(name_file_new)
name_file_old = input("请输入您要修改内容的文件名：")
file_content_old = input("请输入您要替换的旧内容：")
file_content = input("请输入您要修改的文件内容：")
name_file_new = input("请输入您更改后的文件名：")
file(name_file_old,file_content_old,file_content,name_file_new)

#代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a=10
b=20
def test5(a,b):
    print(a,b)
    # c = test5(b,a)
    # print(c)
print(test5(1,2))
