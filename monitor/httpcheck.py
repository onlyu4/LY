import requests
import socket
import json
import time

headre = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'}

urls = []
count = 0
with open("http.list","r") as f:
    for i in f:
        urls.append(i.strip().split("_fen_"))

def dingding(massage,token):
    websock =f'https://oapi.dingtalk.com/robot/send?access_token={token}'
    headers = {"Content-Type":"application/json"}
    data = {"msgtype": "text", "text": {"content":massage}}
    res = requests.post(websock,headers=headers,data=json.dumps(data))
    print(res.text)

count = 0
for i in urls:
    res = requests.get(f"https://{i[1]}",timeout=5,allow_redirects=False)
    print(res.status_code)