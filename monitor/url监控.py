import requests
import time
import json
import socket

headres = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}
urls = []
hostname = socket.gethostname()
with open("2.txt","r",encoding="utf-8") as f:
    for i in f:
        urls.append(i.strip().split("_fen_"))

#钉钉机器人
def dingding(massage,token):
    websock =f'https://oapi.dingtalk.com/robot/send?access_token={token}'
    headers = {"Content-Type":"application/json"}
    data = {"msgtype": "text", "text": {"content":massage}}
    res = requests.post(websock,headers=headers,data=json.dumps(data))
    print(res.text)

def inspect():
    for i in urls:
            count = 0
            while True:
                try:    #异常处理
                    if "HEAD" in i:
                        res = requests.head(i[0], timeout=2, allow_redirects=False, headers=headres)
                    elif "POST" in i:
                        res = requests.post(i[0], timeout=2, allow_redirects=False, headers=headres)
                    else:
                        res = requests.get(i[0], timeout=2, allow_redirects=False, headers=headres)
                except Exception as err:
                    time.sleep(5)     #出现异常停止
                   # print(count)
                    if count > 2:       #判断count是否大于2 如果大于2发送钉钉报警并结束循环
                        dingding(f"请求超时{i[0]}\n--from {hostname}",i[1])
                        break
                    count+=1
                    continue    #count 不大于2进行下次循环
                #判断状态码，不为200发送钉钉报警并结束循环
                if res.status_code != 200:
                    dingding(f"状态码不为200\t{i[0]}\t{res.status_code}\n--from {hostname}",i[1])
                    break
                break
inspect()