import requests
import re
import urllib
from urllib.request import urlopen
import json
# header = {"User-Agent":
#                 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
url = "https://www.dytt8.net/"
# req = requests.get(url,headers=header)
# print(req.headers)
def gain_url():
    url_list = []
    url_son = []
    req = urlopen(url).read().decode("gbk")
    son_url = re.finditer(r"最新电影下载</a>]<a href='(?P<url>.*?)'>",req)
    for i in son_url:
        url_list.append(i.group("url"))
    for i in url_list:
        url_son.append(url+i)
    return url_son
print(gain_url())

def movie_info(gain_url):
    all_info = []
    for item in gain_url:
        movie_dict = {} #用于存储每个电影的信息
        content = urlopen(item).read().decode("gbk")
        object = re.compile(
            r'<div id="Zoom".*?◎片　　名(?P<film_name>.*? )<br />.*?◎主　　演(?P<actors>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)">',
            re.S)
        new_obj = object.finditer(content)
        for i in new_obj:
            movie_name = i.group("film_name")
            movie_url = i.group("download_url")
            main_actors = i.group("actors")
            print(main_actors)
            main_actors1 = main_actors.replace("<br />", "").replace("\u3000", " ").replace(" ", " ").strip().split(
                "    ")
        movie_dict["name"] = movie_name
        movie_dict["actors"] = main_actors
        movie_dict["url"] = movie_url
        all_info.append(movie_dict)
        with open("2.txt","w",encoding="utf-8") as f:
            for index, info in enumerate(all_info, 1):
                temp = {index: info}
                str_info = json.dumps(temp, ensure_ascii=False)
                f.write(str_info + "\n")
movie_info(gain_url())

