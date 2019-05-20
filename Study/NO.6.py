class car():
    #方法
    def fly(self):
        print("fly")
    def jump(self):
        print("jump")
    def run(self):
        print("running")
    #属性
    def __init__(self,color,price):     #__init__初始化 self是对象的本身
        self.color = color
        self.price = price
c = car("红色",1200)
print(c.color,c.price)

class person:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def chi(self,food):
        print(f"s={self.name}在吃{food}")

p = person("zhangsan","男",22)
p.chi("冰淇凌")


class singer:
    def __init__(self,name,sex,age,songs=[]):
        self.name = name
        self.sex = sex
        self.age = age
        self.songs = songs
    def singing(self,song):
        print(f"{self.name}在唱{song}")

    def yanchanghui(self):
        for i in self.songs:
            self.singing(i)

p = singer("汪峰","男","30",["北京","怒放的生命"])
p.yanchanghui()


class atm:
    def __init__(self,username,passwd,menoy=1000):
        self.username = username
        self.passwd = passwd
        self.menoy = menoy

    def very(self):
        if self.username == "admin" and self.passwd == "123456":
            user_input = input("存钱或者取钱.....")
            if user_input == "存钱":
                self.Deposit()
            else:
                self.very()
        else:
            print("账号或密码错误")

    def Deposit(self):
        self.very()
        user_input = input("请输入您要取的金额....")
        user_input = int(user_input)
        if user_input > self.menoy:
            pass


    def take(self):
        pass


class zhangsan:
    def eat(self):
        print("eating.....")

class wangwu(zhangsan):
    pass

wang = wangwu()
wang.eat()

class person:
    country = "中国"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def func(cls):
        print(cls,"func")

p1 = person("zhangsan",22,"男")
p2 = person("lisi",22,"男")
person.country = "民国"

print(p1.country)
print(p2.country)

person.func()

class person:
    def __init__(self,name,sex,birthyear):
        self.name = name
        self.sex = sex
        self.birthyear = birthyear
    @property   #把方法的调用方式改编成编程
    def age(self):
        return 2019 - self.birthyear

p1 = person("zhangsan","男",1997)
print(p1.age)

class persom:
    def __init__(self,name):
        self.name = name

    def play(self,phone):
        pass


class phone:
    def __init__(self,name):
        self.name = name


    def run_CHIJI(self):
        print(f"{self.name}玩吃鸡")

person_1 = persom("张三")
phone_1 = phone("小米")
person_1.play(phone_1)

class teacher:
    def __init__(self,name):
        self.name = name

    def teac(self):
        print(f"{self.name}在上课")

class student:
    def __init__(self,name):
        self.name = name

    def stud(self):
        print(f"{self.name}在学习")

teach = teacher("wangwu")
stu1 = student("zhangsan")

teach.teac()
stu1.stud()