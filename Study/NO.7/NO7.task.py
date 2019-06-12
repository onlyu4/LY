'''
1、new方法和init方法执行的执行顺序
    __new__负责对象的创建，__init__负责对象的初始化，__new__先被执行

2、call方法在什么时候被调用
    在对象绑定类方法的时候调用

3、请用写一个类，用反射为这个类添加一个静态属性
'''

class animal:
    def __init__(self,name):
        self.name = name
    @staticmethod
    def talk():
        print("1111")
s = animal("dog")
s.name()



"""
先把三个类定义出来,并设置对应属性
"""
import getpass

class Student():
    """
    1、查看所有课程
    2、选择课程
    3、查看所选课程
    4、退出程序
    """
    operate_list = ["show_course","select_course","show_selected_course","exit"]

    def __init__(self,name):
        self.name = name
        self.course = []

    def show_course(self):
        """查看可选课程"""
        print("查看可选课程")

    def select_course(self):
        """选择课程"""
        print("选择课程")

    def show_selected_course(self):
        """查看已选课程"""
        print("查看已选课程")

    def exit(self):
        """退出"""
        print("退出")


class Manager():
    """
        1、创建课程
        2、创建学生学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、退出程序
    """
    operate_list = ["craete_course","create_student","show_courses","show_students","show_students_course","exit"]

    def __init__(self,name):
        self.name = name

    def craete_course(self):
        """创建课程"""
        print("创建课程")

    def create_student(self):
        """创建学生账号"""
        print("创建学生账号")

    def show_courses(self):
        """查看课程"""
        print("查看课程")

    def show_students(self):
        """查看课学生"""
        print("查看课程")

    def show_students_course(self):
        """查看学生选课情况"""
        print("查看学生选课情况")

    def exit(self):
        """退出"""
        print("退出")

class Course():
    def __init__(self,name,price,teacher):
        self.name = name
        self.price = price
        self.teacher = teacher


def login():
    usr = input("username :").strip()
    pwd = input("password :").strip()
    # pwd = getpass.getpass("password :").strip()  #在windows控制台可实现密文输入密码

    with open("userinfo") as f:
        for line in f:
            username,password,ident = line.strip().split("|")
            if username == usr and password == pwd:
                return {"name":username,"indentfy":ident,"auth":True}
        else:
            return {"name": usr, "indentfy": None, "auth": False}


def main():
    """程序入口"""
    print("\033[0;32m欢迎使用学生选课系统\033[0m")

    ret = login()
    if ret["auth"]:
        print("\033[0;32m登陆成功,欢迎%s:%s\033[0m"%(ret["indentfy"],ret["name"]))

        if ret["indentfy"] == "Manager":
            obj = Manager(ret["name"])
            for num,opt in enumerate(Manager.operate_list,1):
                print(num,opt)

            while True:
                inp = int(input("请选择要做的操作:"))
                if inp == 1:
                    obj.craete_course()
                elif inp == 2:
                    obj.create_student()
                elif inp == 3:
                    obj.show_courses()
                elif inp == 4:
                    obj.show_students()
                elif inp == 5:
                    obj.show_students_course()
                elif inp == 6:
                    obj.exit()
                else:
                    print("输入序号错误")

        else:
            if ret["indentfy"] == "Student":
                obj = Student(ret["name"])
                for num, opt in enumerate(Student.operate_list, 1):
                    print(num, opt)
            while True:
                inp = int(input("请选择要做的操作:"))
                if inp == 1:
                    obj.show_course()
                elif inp == 2:
                    obj.select_course()
                elif inp == 3:
                    obj.show_selected_course()
                elif inp == 4:
                    obj.exit()
                else:
                    print("输入序号错误")
    else:
        print("\033[0;32m登陆失败\033[0m")

main()


