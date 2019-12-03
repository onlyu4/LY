
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
import os
import re

#请求头
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
url = "https://www.dy2018.com/"
req = requests.get(url)
req.encoding = "gbk"
urls = re.compile(r"2019新片精品.*?<ul>(?P<ul>.*?)</ul>",re.S)
# print(url.findall(req.text))
# 获取到匹配的内容
count = urls.search(req.text)
# print(count.group("ul"))

# 拿到子页面的链接
count_url = re.compile(r"<li><a href='(?P<url>.*?)'")
for i in count_url.findall(count.group("ul")):
    # 拼接url
    url = f"https://www.dy2018.com/{i}"
    print(url)
    reqs = requests.get(url)
    reqs.encoding = "gbk"
    try:
        movie = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie_name>.*?)<br />',re.S)
        movie_content = movie.search(reqs.text)
        print(movie_content.group("movie_name"))
    except AttributeError:
        print("正则不正确")






# 拼接电影的url





