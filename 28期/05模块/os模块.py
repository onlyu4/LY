
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
import os
#创建多级目录
os.makedirs("a/b/a/c")

#创建一个目录
os.mkdir("路径")

#删除多级目录
os.removedirs("路径")

#删除一个目录
os.rmdir("路径")

def dir(path,ceng):
    lst = os.listdir(path)
    for name in lst:
        file_path = os.path.join(path, name)
        if os.path.isdir(file_path):
            print("\t"*ceng,name)
            dir(file_path,ceng+1)
        else:
            print("\t"*ceng,name)
dir("C:\\git\\LY\\28期",0)

for root,dirs,files in os.walk("/"):
    for dir in dirs:
        print(os.path.join(root,dir))
    for f in files:
        print(os.path.join(root,f))

#更换工作目录
os.chdir("相对路径")

#