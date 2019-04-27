#迭代器
lis = ["苍穹幕落太刀","超大陆","七宗罪","增幅券"]
it = lis.__iter__()     #拿到lis的迭代器
#print(it)
print(it.__next__())    #取到迭代器的值
print(it.__next__())
print(it.__next__())

lis_1 = ["张三","李四","王五"]
it_1 = lis_1.__iter__()
while True:
    try:
        print(it_1.__next__())
    except StopIteration:
        break

from collections.abc import Iterable,Iterator   #Iterable判断变量是否为可迭代对象，Iterator判断是否为迭代器

def func(n):
    if isinstance(n,Iterable):
        for i in n:
            print(i)
    else:
        print(n)
func("大家好")

#生成器
#生成器的本质是迭代器

def gen():
    print("abcd")
    yield       #yield是一个生成器函数，会创建一个生成器给你，将函数分段执行
    print("1234")
    yield   #执行到下一个yield
gens = gen()
#gens.__next__()     #需要调用__next__()方法才能使生成器执行一次

def other():
    for i in range(100):
        yield "第"+str(i+1)

s = other()
#print(s.__next__())


lis_2 = ["第%s天"% i for  i in range(1,29)]
print(lis_2)

lst_3 = ["欧阳娜娜", "张崔猛", "欧阳难过", "张亚无照", "胡一飞", "胡怎么飞", "张炸辉"]
lis_3 = []
for i in lst_3:
    if i.startswith("张"):
        lis_3.append(i)
print(lis_3)

print([i for i in lst_3 if i.startswith("张")])

#使用列表推导式得到[1, 4, 9, 16, 25, 36]
print([i*i for i in range(1,7)  ])
# 在[3,6,9]的基础上推到出[[1,2,3], [4,5,6],[7,8,9]]
print([[i-2,i-1,i-0]for i in [3,6,9]])

lis_4 = ["张三","李四","王五"]
dic = {}
for i in range(len(lis_4)):
    dic[i] = lis_4[i]
print(dic)

print({ i :lis_4[i] for i in range(len(lis_4))})

#匿名函数
fun = lambda i :i*i
print(fun(10))

def func_1(n):
    print(len(n))
func_1("hfdjshfksd")

lis_5 = ["波多野结衣","范冰冰","张三","老男孩"]

def func_2(i):
    return len(i)
s = sorted(lis_5,key=func_2)
print(s)

lis_6 = [{"id":1, "name":'alex', "age":18},
 {"id":2, "name":'wusir', "age":16},
 {"id":3, "name":'taibai', "age":17}]

def func_3(i):
    return i["age"]
s = sorted(lis_6,key=func_3)
print(s)

#装饰器
def wapper(fn):
    def innter():
        print("222")
        fn()
        print("33333")
    return innter()
@wapper
def func_4():
    print("1111")
