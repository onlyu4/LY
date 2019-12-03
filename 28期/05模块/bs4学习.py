
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
from bs4 import BeautifulSoup
import requests
url = "http://www.umei.cc/meinvtupian/meinvxiezhen/"
req = requests.get(url)
req.encoding = "utf-8"
#创建一个soup的对象
soup = BeautifulSoup(req.text,"lxml")

#打印title
# print(soup.title)

#打印head
# print(soup.head)

#打印a标签
# print(soup.a)

#打印p标签
# print(soup.p)
#
# print(soup.name)
# print(soup.head.name)

#打印标签的属性
# print(soup.a.attrs)
# print(soup.p.attrs["class"])

#NavigableString获取标签的内部文字
print(soup.p.string)

#BeautifulSoup对象表示的是一个文档的全部内容,大部分时候,可以把它当作 Tag 对象

#tag 的 .content 属性可以将tag的子节点以列表的方式输出
# print(soup.div.contents)

#.children它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
# print(soup.div.children)
# for i in soup.div.children:
#     print(i)

#.descendants属性可以对所有tag的子孙节点进行递归循环
for i in soup.p.descendants:
    print(i)

#


