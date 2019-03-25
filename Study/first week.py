'''
简述变量的命名规范：
    1、变量名已字母货数字开头，单词之间最好用下划线连接，符号不能作为变量名的开头
    2、常量用全大写字母命名
    3、变量名最好用驼峰式或者下划线式


name=input(">>>>")，name变量是什么数据类型
    str


if条件语句的基本结构
    if  代码块
    elif  代码块
    else
        代码块


用print打印出下面内容：文能提笔安天下,  武能上马定乾坤.  心存谋略何人胜, 古今英雄唯是君.

print("文能提笔安天下,\n武能上马定乾坤.\n心存谋略何人胜,\n古今英雄唯是君.")


利用if语句写出猜大小的游戏：设定一个理想数字比如：66，让用户输入数字，
如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

number = "66"
guess_number = input("Please enter your guessed number:")
if guess_number >number:
    print("is  big....")
elif guess_number < number:
    print("is  small.....")
else:
    print("you are good")


提示用户输入他的年龄，进行判断

age = int(input("Please enter your age:"))
#age = int(age)
if age < 10:
    print("小屁孩")
elif age < 20:
    print("青春期叛逆的小屁孩")
elif age < 30:
    print("开始混社会的小屁孩")
elif age < 40:
    print("老大不小了，赶紧结婚生个小屁孩")
elif age < 50:
    print("家里有个不停话的小屁孩")
elif age < 60:
    print("自己马上变成不听话的老屁孩")
elif age < 70:
    print("或者还不错的老屁孩")
elif age < 90:
    print("人生块结束了的老屁孩")
else:
    print("再见了，这个世界")


单行注释及多行注释
    单行注释   #
    多行注释   六个单引号括起来


简述你所知道的python3.x和pyth2.x的区别

提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你是傻逼么

imp = input("请输入麻花藤：")
if imp != "麻花藤":
    print("你是傻逼么")
else:
    print("你真聪明")

使用while循环输入 1 2 3 4 5 6     8 9 10

count = 0
while count <10:
    count += 1
    if count == 7:
        continue
    print(count)


求1-100的所有数的和

count = 0
nub = 0
while count <=100:
    nub = count + nub
    if count == 100:
        print(nub)
    count += 1

输出 1-100 内的所有奇数

count = 1
while count <101:
    print(count)
    count += 2

输出1-100内的所有偶数
for i in range(1,101):
    if i%2 == 0:
        print(i)

求1-2+3-4+5 ... 99的所有数的和


count = 1
nub = 0
while count <100:
    if count % 2 != 0:
        nub = nub + count
    else:
        nub = nub - count
    count += 1
print(nub)
'''


#用户登陆程序
count = 1
while True:
    user = input("Please enter your username>>>>>")
    passwd = input("Please enter your password>>>>")
    if user == "admin" and passwd == "123456":
        print("welcom to login.....")
        break
    else:
        print("user or passwd is error, you have %s opportunity"%(4-count))
        if count == 4:
            break
    count += 1