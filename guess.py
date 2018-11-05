age_of_ly = 22
count = 0
while count < 3:    #count<3时，执行下面的循环
    guess_age = int(input("guess age:"))
    if guess_age == age_of_ly:
        print("yes,you are very goog!!!")
        break  #上面条件成立时结束循环
    elif guess_age > age_of_ly:
        print("Think smaller...")
    else:
        print("Think bigger...")
    count +=1   #每次循环 count+1
    if count == 3:    #如果count=3 执行下面判断
        counttine_confirm = input("Do you want to keep guessing..?")
        if counttine_confirm != "n":    #如果输入的不等于n，则count=0重新开始循环
            count = 0

#else:
   # print("You've guessed it too many ti33mes")#正常跳出循环时，输出这句话