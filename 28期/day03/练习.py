#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？

#1、写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新的内容返回给带调用者
dict = {"k1":"v1v1","k2":[11,22,33,44]}
def dict_len(dict):
    dict_new = {}
    for k,v in dict.items():    #取到字典的key和value
        if len(v) > 2:      #如果val的长度大于2
            dict_new[k] = v[:2]     #字典的value就取字符串的前两位
    return dict_new
ret = dict_len(dict)
print(ret)

#2、写函数，此函数直接收一个参数，且参数是列表，将传入的列表返回给调用者是一个字典，键值对对应为列表的索引和对应的元素
list = [11,22,33]
def key_value(list):
    dict = {}
    for i in range(len(list)):  #取到列表的索引
        dict[i] = list[i]       #字典的key = 列表索引对应的元素
    return dict
ret = key_value(list)
print(ret)

#3、写函数，用户传入修改的文件名，与要修改的内容。执行函数，完成文件的批量修改操作
import os
def reivse(file,old,new):
    with open(f"{file}.txt","r",encoding="utf-8")as f,open(f"{file}.txt.bak","w",encoding="utf-8")as f2:
        for i in f:
            if old in i:
                f2.write(i.replace(old,new))
            else:
                f2.write(i)
                print("你要修改的内容不存在")
    os.remove(f"{file}.txt")
    os.rename(f"{file}.txt.bak", f"{file}.txt")

reivse("1","李四","张三")






