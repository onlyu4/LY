# lst = ["独孤求败", "乔峰", "扫地僧", "乔峰", '郭靖', "郭靖"]
# print(set(lst))
# f = open("NO3.txt","r",encoding="utf-8")
#print(f.read(6))
# lis_1 = []
# for i in f:
#     lis = i.strip().split(",")
#     #print(lis)
#     dic = {"id":lis[0],"name":lis[1],"price":lis[2]}
#     lis_1.append(dic)
# print(lis_1)
# title_list = f.readline().strip().split(",")
# #print(title_list)
# list_1 = []
# for i in f:
#     list = i.strip().split(",")
#     # print(list)
#     dict = {}
#     for i in range(len(title_list)):
#         dict[title_list[i]] = list[i]
#     list_1.append(dict)
# print(list_1)
# f = open("haha","a",encoding="utf-8")
# f.write("NSF教授副教授的")

# def game(tools):
#     print("打开电脑")
#     print("打开%s"%tools)
#     print("打开csgo")
#     print("biu....biu....biu")
#     return "休息啦"
# print(game("steam"))
# def login():
#     username = input("请输入账号")
#     passwd = input("请输入密码")
#     if username == "admin" and passwd == "123":
#         return True
#     else:
#         return False
# print(login())

# def compare(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(compare(3,3))

# def compare(a,b):
#     return a if a > b else b
#
# print(compare(12,18))

# def user_input(name,age,sex="男"):
#     print(name,sex,age)
# user_input("张三",22)
# user_input("李四",28,"女")

def food(*args):
    print(args)
food("大米饭","酸菜鱼","红烧肉")

def foods(**kwargs):
    print(kwargs)
foods(a = "大米饭",b = "酸菜鱼")