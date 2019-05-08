import requests
import re
import urllib
from urllib.request import urlopen
# header = {"User-Agent":
#                 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
url = "https://www.dytt8.net/"
# req = requests.get(url,headers=header)
# print(req.headers)

req = urlopen(url).read().decode("gbk")
son_url = re.finditer(r"最新电影下载</a>]<a href='(?P<url>.*?)'>",req)
url_list =[]
for i in son_url:
    url_list.append(i.group("url"))
print(url_list)