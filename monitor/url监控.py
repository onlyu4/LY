#-*- coding:utf-8-*-
#Author:liuyan
import requests
import time
import json

all_urls = [
    "https://www.bai.com",
    "https://www.google.com",
    "http://www.niuguwang.com"
]
headres = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}
#钉钉机器人
def dingding(massage):
    websock ='https://oapi.dingtalk.com/robot/send?access_token=de95405b0bdfa46ea4f3b621516427102fcf1967ffe0ab12ca8d031205d5bbe1'
    headers = {"Content-Type":"application/json"}
    data = {"msgtype": "text", "text": {"content":massage}}
    res = requests.post(websock,headers=headers,data=json.dumps(data))
    print(res.text)

def inspect():
    count = 0
    for i in all_urls:
        count = 0
        while True:
            try:    #异常处理
                res = requests.get(i, timeout=2,allow_redirects=False)
            except Exception as err:
                time.sleep(10)     #出现异常停止
               # print(count)
                if count > 2:       #判断count是否大于2 如果大于2发送钉钉报警并结束循环
                    dingding("请求超时%s"%i)
                    break
                count+=1
                continue    #count 不大于2进行下次循环
            #判断状态码，不为200发送钉钉报警并结束循环
            if res.status_code != 200:
                dingding("%s    %s"%(i,res.status_code))
                break
            break
inspect()