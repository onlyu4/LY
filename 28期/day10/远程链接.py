
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

import paramiko
import sys

def process_bar(now,totle):
    baifen = (now * 100 // totle)
    sys.stdout.write(f"\r[{baifen  * '='}~{baifen}%]")


trans = paramiko.Transport(("123.206.16.61",22))
trans.connect(username="root",password="nidaye..!")
#ssh通信
ssh = paramiko.SSHClient()
#
# #绑定链接
ssh._transport = trans
#
# #执行命令
stdin, stdout, stderror = ssh.exec_command("ls")
print(stdout.read().decode("utf-8"))

# ftp = trans.open_sftp_client()
# ftp.put("1.jpg","高清美女写真集.jpg",callback=process_bar)
# print(111)