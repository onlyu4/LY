#-*- coding:utf-8-*-
#Author:liuyan

import requests
import json
import time
def dingding(massage):
    websock ='https://oapi.dingtalk.com/robot/send?access_token=29723653800ebb7ecbde0da7296cecfc47ef1d4b1e17543c82731714bde2a23a'
    headers = {"Content-Type":"application/json"}
    data = {"msgtype": "text", "text": {"content":massage}}
    res = requests.post(websock,headers=headers,data=json.dumps(data))
    #print(res.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}
url = ["https://hq.bitmixs.com/v1/api/quote/cacheAlert"]
for i in url:
    count = 0
    while True:
        try:  #监测是否超时，异常检查
            res = requests.get(i, headers=headers, timeout=0.5)
        except Exception as err:
            time.sleep(5)   #三次超时发出报警
            if count > 2:
                dingding("访问超时%s"%i)
                break
            count += 1
            continue
        inform = json.loads(res.text)   #检查 dict中的value是否为status
        if inform["status"] != 200:
            dingding("status不为200，请检查%s"%i)
            break
        break










