#import sys    #调用模块
#print(sys.path)  #打印环境变量
'''
import os
#cmd = os.system("dir")  #system，只执行命令，不保存结果
#cmd = os.popen("dir").read()  #popen执行命令的结果保存到内存中，需要用 .read()读取出来
cmd = os.mkdir() #创建目录
print(cmd)
'''



'''
#列表
names = ["ZhangSan","LiSi","Wangwu","ChenLiu"]
#print(names[0],names[3])  #取列表中的第一个、第四个值
#print(names[0:3])  #取列表中第一个到第三个的值
#print(names[-3:-1])  #取列表中第二到第三个值
names.append("WangErMazi")  #在列表中插入值（默认在最后）
names.insert(1,"WANGWU")    #在列表第二个值前面增加个值
print(names.index("WANGWU"))  #查找值在哪个位置
print(names.count("WANGWU"))   #统计一共有多少相同的值
names.sort()   #排序
names.remove("WANGWU")      #删除列表中的值
names.extend(表名)  #合并表
print(names)
'''
'''
元组
names = ("zhangsan","lisi","wangwu")
#print(names.count("zhangsan"))   #统计有多少相同的值
print(names.index("zhangsan"))    #查找值在哪个位置
'''
'''
#购物车程序
balance = input("请输入您的工资：")
shopping_list = []
goods_list = [
    ("IPhone",12999),
    ("Book",200),
    ("computer",5999),
    ("coffee",34),
]
if balance.isdigit():
    balance = int(balance)
    while True:
        for index,i in enumerate(goods_list):
             #print(goods_list.index(i),i)
             print(index,i)
        user_choice = input("你想买什么？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice > len(goods_list) and goods_list >=0:
                p_i = goods_list[user_choice]
                if p_i[1] <= balance:
                    shopping_list.append(p_i)
                    balance -= p_i[1]
                    print("%s已经加入购物车，你还有%s"%(p_i,balance))
                else:
                    print("您的余额只有%s了，请充值"%(balance))
            else:
                print("商品不存在")
        elif user_choice == "q":
            print("-------shopping_list-----------")
            for p in shopping_list:
                print(p)
            print("您的钱还有",balance)
            exit()
        else:
            print("错误选项")
'''
