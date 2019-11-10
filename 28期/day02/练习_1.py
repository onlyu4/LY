
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

dict = {
    "name":["alex",2,3,5],
    "job" : "teacher",
    "oldboy" : {'alex':['python1','python2',100]}
}

#1、将name对应得列表追加一个元素wusir
dict["name"].append("wusir")
#print(dict)

#2、将name对应得列表alex首字母大写
for i in dict["name"]:
    if str(i).startswith("a"):
       dict["name"][0] = i.capitalize()
#print(dict)

#3、在oldboy对应得字典中加一个键值对“老男孩”，Linux
dict["oldboy"]["老男孩"] = "linux"
#print(dict)

#4、将oldboy对应字典中得alex对应列表中得python2删除
#print(dict["oldboy"]['alex'][1])


#5、使用for循环对s=“abcdefg”进行循环，每次打印字符后都加上sb
s = "abcdefg"
for i in s:
    print(f"{i}sb")


#6、计算用户输入中有几个整数
# number = 0
# count = input("请输入内容：")
# for i in count:
#     if i.isdigit():
#         number+=1
# print(number)

#制作趣味模板
# name = input("情输入你的名字：")
# place = input("请输入你要去的地点")
# hobby = input("请输入你的爱好")
# print(f"亲爱的{name}喜欢在{place}干{hobby}")

while 1:
    mode = input("请选择你回家的方式(A/B/C)：").strip()
    if mode.isalpha():
        if mode.upper() == "A":
            print("走大路回家")
            second_mode = input("选择公交还是步行？：")
            if second_mode == "公交":
                print("十分钟到家")
                break
            elif second_mode == "步行":
                print("二十分钟到家")
                break
            else:
                print("请输入“公交/步行")
        elif mode.upper() == "B":
            print("走小路回家")
            break
        elif mode.upper() == "C":
            print("绕道回家")
            third_mode = input("是选择去游戏厅还是网吧？")
            if third_mode == "游戏厅":
                print("一个半小时到家，爸爸在家拿棍子在等你")
                continue
            elif third_mode == "网吧":
                print("两个小时到家，妈妈已经做好了战斗准备")
                continue
            else:
                print("请输入网吧/游戏厅")
