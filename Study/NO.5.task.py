import time
#计算两个格式化时间之间差了多少年月日时分秒
first_time = "1989-01-01 12:00:00"
second_time = "1989-01-01 14:35:00"
first_time_stamp = time.mktime(time.strptime(first_time,"%Y-%m-%d %H:%M:%S"))
second_time_stamp = time.mktime(time.strptime(second_time,"%Y-%m-%d %H:%M:%S"))
#print(first_time_stamp,second_time_stamp)
time_diff = (second_time_stamp - first_time_stamp)
diff_min = time_diff // 60
#print(diff_min)

diff_hours =  diff_min//60
#print(diff_hours)
min_diff = diff_min % 60
#print(min_diff)
print(f"相差了{diff_hours}小时{min_diff}分钟")

#计算当前时间所在月1号的时间戳
# import time
#
# str_time = time.strftime("%Y-%m")
# #struct_time = time.strptime(str_time,"%Y-%m")
# struct_time = time.strptime(str_time+"-01","%Y-%m-%d")
# print(time.mktime(struct_time))


#生成一个6位随机验证码(包含数字和大小写字母)
import random
def make_code():
    res = ""
    for i in range(6):
        number = str(random.randint(0,9))   #取随机数0-9
        letter = chr(random.randint(65,90))     #取随机小写字母a-z
        LETTER = chr(random.randint(97,122))    #取随机大写字母A-Z
        res += random.choice([number,letter,LETTER])    #拼接数字和字母
    return res
print(make_code())

#发红包、制定金额和个数随机分配红包金额
def red_envelopes():
    money = 100
    lis = []
    for i in range(10):
        amount = random.randint(1, 100)
        lis.append(amount)
    for i in lis:
        each = (i / sum(lis)) * money
        print(round(each,2))
red_envelopes()
#分别列出给定目录下所有的文件和文件夹
import os
print(os.listdir("C:/"))

#获取当前文件所在目录
print(os.getcwd())

#在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
# os.mkdir("c:/test")
# with open("c:/test","w",encoding="utf-8") as f:
#     f.write("test")

#计算某路径下所有文件和文件夹的总大小
print(os.path.getsize(r"c:\Users"))







