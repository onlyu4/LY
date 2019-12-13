
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
for i in range(1,1000):
    url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
    urls = url.replace("1.shtml",f"{i}.shtml")
    req = requests.get(urls)
    print(urls)
    soup = BeautifulSoup(req.text,"html.parser")
    table = soup.find("table",attrs={"class":"hq_table"})
    # print(table)
    trs = table.find_all("tr")[1:]  # 表头不要
    with open("新发地.csv","a",encoding="utf-8") as f:
        for tr in trs:
            tds = tr.find_all("td")
            for i in tds:
                f.write(i.text)
            f.write("\n")

