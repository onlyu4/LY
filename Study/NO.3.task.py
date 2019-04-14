
list_2 = []
with open("a1.txt","r",encoding="utf-8") as f:
    list_1 = f.readline().strip().split(",")  #取表头并进行切片
    #print(list_1)
    for i in f:
        #print(i)
        list = i.strip().split(",")#取到之后的所有内容
        #print(list)
        dic = {}
        for i in range(len(list_1)):    #循环的次数是list_1的长度
            dic[list_1[i]] = list[i]    #定义字典的key和value
        list_2.append(dic)      #将字典添加到列表中
print(list_2)

