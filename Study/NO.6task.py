
#1.类，对象，实例，实例化分别是什么
#     类：事物的抽象，代表着具有相同特征的一类事物
#     对象：具体的某一个事物
#     实例：具体的某一个事物
#     实例化：类————>实例的过程叫做实例化
#
# #2、面向对象的三大特性
#
# #继承：
#     一个类拥有另一个类的所有属性和方法
# #多态：
#     不同的对象，继承相同的父类，调用相同的方法，执行不同的函数
# #封装：
#     隐藏对象的属性和细节，仅对外提供公共的访问方式
#     作用：
#         将业务和实现逻辑解耦
#         提高了代码呃易用性，复用性，安全性


#3、说说python中所说的封装是什么意思？
#     隐藏对象的属性和细节，仅对外提供公共的访问方式
#
# #4、多态是怎么回事？在python中是如何体现的？
#     一类事物有多种形态

#5、说说面向对象中“私有”的概念以及应用
    # 对外变形，对内提供调用，子类无法重新父类私有的方法

#6、在面向对象中有一些被装饰器装饰的方法，先说说有哪些装饰器，再说说这些装饰器的作用，以及装饰之后的效果
    # @classmethod：对类属性进行操作时用此方法
    # @staticmethod：无需实例化
    # @property：将变量转换和变量相同的调用方式


#7、请说明新式类和经典类的区别，至少两个
    # 经典类的继承是深度继承，即从下到上搜索，新式类的继承是采用c3算法
    # 在经典类中，所有的类都是classobj类型，而类的实例都是instance类型。类与实例只有通过__class__属性进行关联

#8、请说出上面一段代码的输出并解释原因？
class Foo:
    def func(self):
        print('in father')
class Son(Foo):
    def func(self):
        print('in son')
s = Son()
s.func()
   # 打印的结果是  in son 因为Son类继承了Foo 并对func方法进行了重写

'''

'''
#作业
#1、类属性和实例属性有什么区别
    # 类属性是实例对象共有的属性
    # 实例属性是实例自己独有的属性
    #
#2、写个实际使用类属性的代码
class People:
    name = "tom"
    age = 18
p = People()
print(p.name,p.age)
    
#3、自己设计场景，并写个封装代码
class House:
    def __init__(self,length,wide):
        self.__length = length
        self.__wide = wide
    def size(self):
        return  self.__length * self.__wide
a = House(20,30)
print(a.size())

#4、写个继承代码

class Father:
    def talk(self):
        print("I'm father")

class Son(Father):
    def func(self):
        pass
p = Son()
p.talk()

#5、写个多态代码


class Animal:
    def talk(self):
        return "我是动物"

class Person(Animal):
    def talk(self):
        return "我是人"

class Cat(Animal):
    def talk(self):
        return "我是猫"
person = Person()
cat = Cat()
print(cat.talk())

#6、写个组合代码

class Arms:
    def arms1(self):
        return "AK"

    def arms2(self):
        return "M4A1"
class Person:
    def __init__(self,name):
        self.name = name
        self.arms = Arms()
p = Person("小明")
print(p.name,p.arms.arms1())





