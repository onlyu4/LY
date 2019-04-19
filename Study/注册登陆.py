def option():
    user_input = input("注册  登陆  退出  购物")
    if user_input == "注册":
        register()
    elif user_input == "登陆":
        login()
    elif user_input == "退出":
        pass
    else:
        print("请输入正确的选项")


def register():
    fag = True
    while fag:
        user_name = input("用户名：")
        user_passwd = input("密码：")
        with open("user.txt","r+",encoding="utf-8") as f:
            for i in f:
               lis = i.split(" ")
               if user_name == lis[0]:
                   print("用户名已存在！！")
                   continue
               else:
                   f.write("\n%s,%s"%(user_name,user_passwd))
                   print("注册成功！！！")
                   fag = False
#register()
def login():
    count = 1
    while count <= 3:
        user_name = input("用户名：")
        user_passwd = input("密码：")
        with open("user.txt","r",encoding="utf-8") as f:
            for i in f:
                lis = i.split(",")
                if user_name == lis[0] and user_passwd == lis[1]:
                    print("登陆成功")
                    count = 4
                else:
                    print("登陆失败，您还有%s次机会"%(3-count))

                count += 1
option()

