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
import json

class Client:
    def __init__(self):
        self.user_type = None   # 如果管理员登录user_type 就是管理员，如果是学生登录，user_type就是学生

    def login(self):
        while 1:
            username = input("请输入你的账号：")
            passwd = input("请输入你的密码：")
            with open("userinfo.txt","r",encoding="utf-8") as f:
                for i in f:
                    line = i.strip()
                    info = json.loads(line)
                    if info["username"] == username and info["passwd"] == passwd:
                        print("登录成功")
                        if info["type"] == 0:
                            self.user_type = Admin(info["username"],info["passwd"],info["type"])    # 管理员
                        else:
                            self.user_type = Student(info["username"], info["passwd"], info["type"],info["course_list"])    # 学生
                        return
                else:
                    print("账号或密码错误，请重新输入")

    def start(self):
        self.login()
        if self.user_type.user_type == 0:
            self.admin_client()
        else:
            self.student_client()

    def admin_client(self):
       while 1:
            menu = input("1、创建课程\n2、创建学生账号\n3、查看所有课程\n4、查看所有学生的选课情况\n5、退出\n选择你要进行的操作")
            if menu == "1":
               self.user_type.create_course()
            elif menu == "2":
                self.user_type.create_student()
            elif menu == "3":
                self.user_type.shwo_all_course()
            elif menu == "4":
                self.user_type.show_student_course()
            elif menu == "5":
                print("正在退出程序")
                return
            else:
                print("输入你序号有误，请重新输入")

    def student_client(self):
        while 1:
            menu = input("1、查看所有课程\n2、选择课程\n3、查看所选课程\n4、删除已选课程\n5、退出\n选择你要进行的操作")
            if menu == "1":
                self.user_type.show_all_course()
            elif menu == "2":
                self.user_type.choice_course()
            elif menu == "3":
                self.user_type.shwo_my_course()
            elif menu == "4":
                self.user_type.show_student_course()
            elif menu == "5":
                print("正在退出程序")
                return
            else:
                print("输入你序号有误，请重新输入")



class Admin:
    def __init__(self,username,passwd,user_type):
        self.username = username
        self.passwd = passwd
        self.user_type = user_type

    def create_student(self):
        username = input("请输入学生的账号：")
        s = Student(username,"123456","1")  #创建学生对象
        s.write_to_file()

    def create_course(self):
        name = input("请输入你要创建的课程名称")
        c = Course(name)
        c.write_to_file()

    def shwo_all_course(self):
        course_list = Course.get_all_course()
        for i in course_list:
            print(i.name)


    def show_student_course(self):
        pass

class Student:
    def __init__(self,username,passwd,user_type,course_info=None):
        self.username = username
        self.passwd = passwd
        self.user_type = user_type
        self.course_info = course_info if course_info else []

    def write_to_file(self):
        with open("userinfo.txt","a",encoding="utf=8") as f:
            f.write(json.dumps(self.__dict__) + "\n")

    def show_all_course(self):
        list = Course.get_all_course()
        for i in list:
            pass
    def choice_course(self):
        pass
    def shwo_my_course(self):
        list = Course.get_all_course()
        for i in self.course_info:
            print(list[i-1].name)



class Course:
    def __init__(self,name):
        self.name = name
    def write_to_file(self):
        with open("course.txt", "a", encoding="utf-8") as f:
            f.write(self.name + "\n")

    @staticmethod
    def get_all_course():
        list = []   # 拿到课程对象
        with open("course.txt","r",encoding="utf-8") as f:
            for i in f:
                list.append(Course(i.strip()))  #创建课程对象
        return list


if __name__ == '__main__':
    Client().start()