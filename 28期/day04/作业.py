
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
import json
import datetime
#用户名
username = None
#登陆状态
login_stats = False
def home_page():
    while 1:
        user_input = input("欢迎来到博客园首页\n请输入你要操作的序号\n1、请登录\n2、请注册\n3、文章界面\n4、日记界面\n5、注销\n6、退出")
        if user_input == "1":
            login()
        elif user_input == "2":
            register()
        elif user_input == "3":
            article()
        elif user_input == "4":
            diary()
        elif user_input == "5":
            log_off()
        elif user_input == "6":
            break
        else:
            print("请输入正确的序号")

def register():
    global username
    global login_stats
    dict_info = {}
    while 1:
        name = input(" 请输入您要注册的账号：")
        passwd = input("请输入密码：")
        dict_info["name"] = name
        dict_info["passwd"] = passwd
        with open("register.txt", "r", encoding="utf-8") as f:
            f.readline()
            for i in f:
                line = json.loads(i)
                if line["name"] == name:
                    print("用户名已存在")
                    break
            else:
                with open("register.txt", "a", encoding="utf-8") as f:
                    js = json.dumps(dict_info)
                    f.write(js + "\n")
                    print("注册成功！！！")
                    username = name
                    login_stats = True
                    with open(f"{name}.文章.txt","w",encoding="utf-8") as f,open(f"{name}.日记.txt","w",encoding="utf-8")as f2:
                        break

def login():
    global username
    global login_stats
    for i in range(3):
        with open("register.txt","r",encoding="utf-8") as f:
            name = input("请输入你的账号：")
            passwd = input("请输入你的密码：")
            #f.readline()
            for i in f:
                line = i.strip()
                line = json.loads(line)
                if name == line["name"] and passwd == line["passwd"]:
                    username = name
                    login_stats = True
                    print("登陆成功")
                    username = name
                    login_stats = True
                    return
            else:
                print("登陆失败,账号或密码错误")

def log_off():
    global username
    global login_stats
    login_stats =False
    print(f"{username}已退出登陆")

def log(fn):
    def inner(*args,**kwargs):
        s = f"用户:{username}在{datetime.datetime.now()}访问了{fn.__name__}\n"
        with open("blog.log","a",encoding="utf-8") as  f:
            f.write(s)
        ret = fn(*args,**kwargs)
        return ret
    return inner

def lgoni_stats(fn):
    def inner(*args,**kwargs):
        while username == None or lgoni_stats == False:
            login()
        else:
            ret = fn(*args,**kwargs)
            return ret
    return inner
@lgoni_stats
@log
def article():
    while 1:
        user_input = input("请输入你要操作的序号\n1、查看文章\n2、添加文章\n3、删除文章\4返回上一单元")
        if user_input == "1":
            with open(f"{username}.文章.txt","r",encoding="utf-8") as f:
                for i in f:
                    print(i.strip())
        elif user_input == "2":
            with open(f"{username}.文章.txt", "a", encoding="utf-8") as f:
                title = input("请输入文章的标题：")
                content = input("请输入文章的内容：")
                title_info = {}
                title_info["标题"] = title
                title_info["内容"] = content
                f.write(json.dumps(title_info))
        elif user_input == "3":
            with open(f"{username}.文章.txt", "a", encoding="utf-8") as f,open(f"{username}.文章.txt.bak", "a", encoding="utf-8") as f2:
                del_title = input("请输入你要删除的文章：")
                f.readline()
                for i in f:
                    line = json.loads(i)
                    if del_title == line["标题"]:
                        continue
                    f2.write(json.dumps(line))
            os.remove(f"{username}.文章.txt")
            os.rename(f"{username}.文章.txt.bak",f"{username}.文章.txt")
        elif user_input == "4":
            break
@log
@lgoni_stats
def diary():
    while 1:
        user_input = input("请输入你要操作的序号\n1、查看日记\n2、添加日记\n3、删除日记\4返回上一单元")
        if user_input == "1":
            with open(f"{username}.日记.txt", "r", encoding="utf-8") as f:
                for i in f:
                    print(i.strip())
        elif user_input == "2":
            with open(f"{username}.日记.txt", "a", encoding="utf-8") as f:
                # title = input("请输入文章的标题：")
                content = input("请输入文章的内容：")
                title_info = {}
                title_info["时间"] = datetime.datetime.now()
                title_info["内容"] = content
                f.write(json.dumps(title_info))
        elif user_input == "3":
            with open(f"{username}.文章.txt", "a", encoding="utf-8") as f, open(f"{username}.文章.txt.bak", "a",
                                                                              encoding="utf-8") as f2:
                del_title = input("请输入你要删除的日记：")
                f.readline()
                for i in f:
                    line = json.loads(i)
                    if del_title == line["时间"]:
                        continue
                    f2.write(json.dumps(line))
            os.remove(f"{username}.日记.txt")
            os.rename(f"{username}.日记.txt.bak", f"{username}.日记.txt")
        elif user_input == "4":
            break


home_page()