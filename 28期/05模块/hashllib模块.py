
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
import hashlib
uname = "zhangsan"
pwd = "e6ee1dc2e9f6562b5cd86f89f8e4724b"
# obj = hashlib.md5(b"asdasdwh2y723hrgehgahjsfjka")
# obj.update(pwd.encode("utf-8"))
# a = obj.hexdigest()
# print(a)



def my_md5(s):
    obj = hashlib.md5(b"asdasdwh2y723hrgehgahjsfjka")
    obj.update(s.encode("utf-8"))
    value = obj.hexdigest()
    return value

def login():
    name = input("请输入账号：")
    passwd = input("请输入密码：")
    if name == uname and pwd == my_md5(passwd):
        print("登陆成功")
    else:
        print("登陆失败")

#加密文件
f = open("一个文件.txt","rb")
obj = hashlib.md5(b"hfusd9y78yw)U*U(EHFJDK")
for i in f:
    obj.update(i)
print(obj.hexdigest())

