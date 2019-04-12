data = [("iphone x max" , 8888),
        ("macbook" ,12888),
        ("华为p30 pro",6999),
]
shopping_list = []
recharge = input("请输入您要充值的金额：").strip()
if recharge.isdigit():
    recharge = int(recharge)

while True:
    for k,v in enumerate(data):   #打印列表的下标
        print(k,v)
    user_input = input("请输入您要购买的商品编号：")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input < len(data) and user_input >= 0:
            comm = data[user_input]
            if comm[1] <= recharge:
                shopping_list.append(comm)
                recharge -=  comm[1]
                print(comm[1])
            else:
                print("你的还有%s元，请充值"%recharge)
            #print(shopping_list)
        else:
            print("该商品不存在，请重新输入")
    elif user_input.upper() == "N":
       for i in shopping_list:
           print(i)
           print("您还剩余%s元"%(recharge))
           exit()
    elif user_input.upper() == "N":
        break
