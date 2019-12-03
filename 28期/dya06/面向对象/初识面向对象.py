
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

class Car:
    def __init__(self,color,brand,pailing):
        self.color = color
        self.brand = brand
        self.pailiang = pailing

    def run(self):
        print(f"我的{self.color}车在漂移")
        self.fly()

    def fly(self):
        print("我的车在飞")

    def jump(self):
        print("我的车在跳")

c1 = Car("red","布加迪","10L")
# print(c1.color,c1.brand,c1.pailiang)
# c1.run()

class Computer:
    def __init__(self,cpu,men,ssd,gpu):
        self.cpu = cpu
        self.men = men
        self.ssd = ssd
        self.gpu = gpu

    def games(self):
        print("我在打游戏")

    def work(self):
        print("我在工作")

computer_1 = Computer(9700,"32G","1T","ROG_2080ti")
computer_1.games()

computer_2 = Computer(7700,"8G","1T","750")
computer_2.work()


class student:
    country = "China"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        print(f"{self.name}在学习")

    def sleep(self):
        print(f"{self.name}在睡觉")

stu1 = student("张三",20,"男")

stu2 = student("李四","22","女")
print(stu1.country)
student.country = "中国"
print(stu1.country)