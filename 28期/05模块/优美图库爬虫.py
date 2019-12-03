
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

import requests
from bs4 import BeautifulSoup
url = "http://www.umei.cc/meinvtupian/meinvxiezhen/"
photo_list = []
req = requests.get(url)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")
urls = soup.find_all("a", attrs="TypeBigPics")
for i in urls:
    href = i.get("href")
    # 进入相册
    sub_page = requests.get(href)
    sub_page.encoding = "utf-8"
    # print(sub_page.text)
    # 处理子页面内容
    content = BeautifulSoup(sub_page.text,"html.parser")
    div = content.find("div",attrs={"class":"ImageBody"})
    # print(div)
    img = div.find("img")
    # print(img)
    # 拿到相册首页的图片
    src = img.get("src")
    photo_list.append(src)
    #找到下一页的脚本
    script = div.find_next("script").text
    #拿到每个相册的页数
    num = int(script.split(",")[1].strip("\""))
    for i in range(2,num +1):
        # 得到每个相册的子链接
        sub_url = href.replace(".htm", f"_{i}.htm")
        # print(sub_url)
        #请求每个子链接
        sub_req = requests.get(sub_url)
        sub_req.encoding = "utf-8"
        #处理每个页面的内容
        sub_content = BeautifulSoup(sub_req.text,"html.parser")
        # print(sub_content)
        sub_div = sub_content.find("div",attrs={"class":"ImageBody"})
        sub_img = sub_div.find("img")
        sub_src = sub_img.get("src")
        photo_list.append(sub_src)
        # break


    # break

# print(photo_list)
num = 1
for i in photo_list:
    with open(f"图库/{num}.jpg","wb") as f:
        print(f"正在下载{num}张图片")
        f.write(requests.get(i).content)
        print(f"第{num}张图片已下载完成")
        num+=1
