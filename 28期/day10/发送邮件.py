
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

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from  email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


#发件人
sender = "17310958353@163.com"

#准备email
email_list = ["1017433197@qq.com","17310958353@163.com"]
email = MIMEMultipart()
email["Subject"] = "明天出去吃火锅"    # 邮件的标题
email["From"] = sender      # 发件人
email["To"] = ",".join(email_list)    #发送给谁

#邮件正文
# text = MIMEText("test",_subtype="plain",_charset="utf-8")
# email.attach(text)
text = MIMEText("tu:<img src = 'cid:jay'/>",_subtype="html",_charset="utf-8")
email.attach(text)

#图片
photo = MIMEImage(open("1.jpg","rb").read())
photo.add_header("Content-ID","jay")
email.attach(photo)
#发送邮件
smtp = smtplib.SMTP()

# 链接邮件服务器
smtp.connect("smtp.163.com")

#登陆邮箱
smtp.login(sender,"wowangle1")

smtp.sendmail(sender,email_list,email.as_string())

print("OK")