product_list = [                  #建列表
    ("Iphone",999),
    ("Book",20),
    ("apple",5),
    ("computer",5999),
    ("watch",999)
]
shopping_list = []                #临时存放商品列表
salary = input("请输入你的工资")
if salary.isdigit():              #i如果输入的salary的值整数
    salary = int(salary)           #给转成数字
    while True:                 #循环
        for index,item in enumerate(product_list):   #打印商品列表，index为打印列表下标，enumerate为取出index打印出的下标、不用每次都去打印index
            print(index,item)
        user_choice = input("请选择你要购买的商品的编号>>>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:  #判断输入的是否大于等于零，小于列表的长度。len：取列表的长度
                p_item = product_list[user_choice]   # 取商品的价格
                if p_item[1] <= salary:    #如果用户的钱小于等于商品的价格
                    shopping_list.append(p_item)   #将商品加入临时列表
                    salary -=p_item[1]   #扣除钱
                    print("%s已经加入购物车，你还有%s元" %(shopping_list,salary))
                else:    #如果钱不够的话，则输出下面这句话
                    print("你还有%s元，请充值" %(salary))
        elif user_choice == "q":    #如果输入的是q，则打印下面这句话，并退出
            print("------shopping_list--------")
            for p in shopping_list:
             print(p)
            print("你还有%s元"%(salary))
            exit()   #结束循环
        else:#如果输入的超过列表长度的值，那么输出下面这句话，开始新的循环
             print("没有该商品")
