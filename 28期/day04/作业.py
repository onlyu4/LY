
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？
import time
import os
def hone_page():
    global login_status
    while 1:
        user_input = input("欢迎来到博客园首页\n1、请登录\n2、请注册\n3、文章界面\n4、日记界面\n5、注销\n6、退出")
        if user_input == "1":
            login()
        elif user_input == "2":
            register()
        elif user_input == "3":
            article()
        elif user_input == "4":
            diary()
        elif user_input == "5":
            login_status = False
        elif  user_input == "6":
            break

login_status = False
def decorator_login(fn):
    global login_status
    def inner(*args,**kwargs):
        if login_status == True:
            fn(*args,**kwargs)
        else:
            login()
            fn(*args,**kwargs)
    return inner


def register():
    global login_status
    dict_info = {}
    with open("regiser.txt","a",encoding="utf-8")as f:
        name = input("请输入你的账号：")
        passwd = input("请输入密码：")
        dict_info["name"] = name
        dict_info["passwd"] = passwd
        f.write(str(dict_info)+"\n")
        login_status = True

def login():
    global login_status
    with open("regiser.txt","r",encoding="utf-8")as f:
        count = 0
        while count < 3:
            name = input("请输入您的账号：")
            passwd = input("请输入您的密码：")
            for i in f:
                dict_info = eval(i.strip())
                if dict_info["name"] == name and dict_info["passwd"] == passwd:
                    print("恭喜你登陆成功！")
                    login_status = True
                    return
                else:
                    register()
    return


def article():
    while 1:
        user_input = input("1、查看文章\n2、添加文章\n3、删除文章\n4、返回上一单元")
        if user_input == "1":
            article_see()
        elif user_input == "2":
            article_add()
        elif user_input == "3":
            article_del()
        elif user_input == "4":
            break
        else:
            print("请选择正确的选项")
def article_see():
    with open("article.txt", "r", encoding="utf-8")as f:
        for i in f:
            print(i)

def article_del():
    article_see()
    with open("article.txt", "r", encoding="utf-8") as f, open("article.txt.bak", "w", encoding="utf-8") as f2:
        del_input = input("请输入你要删除的文章标题：")
        for i in f:
            info = eval(i.strip())
            if info["标题"] == del_input:
                continue
            f2.write(str(info))
    os.remove("article.txt")
    os.rename("article.txt.bak", "article.txt")

def article_add():
    dict = {}
    with open("article.txt", "a", encoding="utf-8") as f:
        title = input("请输入文章的标题：")
        content = input("请输入文章的内容：")
        dict["标题"] = title
        dict["内容"] = content
        f.write(str(dict))
@decorator_login
def diary():
    while 1:
        user_input = input("1、查看日记\n2、添加日记\n3、删除日记\n4、返回上一单元")
        if user_input == "1":
            diary_see()
        elif user_input == "2":
            diary_add()
        elif user_input == "3":
            diary_del()
        elif user_input == "4":
            break
        else:
            print("请输入正确的选项")
def diary_add():
        with open("diary.txt","a",encoding="utf-8") as  f:
            input_time = time.strftime("%Y-%m-%d",time.localtime())
            diary_content = input("请写入你要写的内容的日记：")
            f.write(f"{input_time}***{diary_content}" + "\n")

def diary_see():
    with open("diary.txt","r",encoding="utf-8") as f:
        #f.readline()
        count = 0
        for i in f:
            count += 1
            print(count,i.strip().split("***"))


def diary_del():
    diary_see()
    with open("diary.txt", "r", encoding="utf-8") as f,open("diary.txt.bak","w",encoding="utf-8") as f2:
        user_input = input("请输入你要删除的日记日期")
        f.readline()
        for i in f:
            if user_input in i.strip().split("***"):
                continue
            f2.write(str(i))
    os.remove("diary.txt")
    os.rename("diary.txt.bak","diary.txt")
hone_page()

#print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
