#conding=utf-8

import requests
import json

url="http://192.168.1.144:8090/api/Login/Login"
data={
	"UserName":"junyi.wang@improve-quality.com",
	"Password":"26614dd7cf54cf906ca4996a20a33686"
}
#jsondata = json.dumps(data)
#print(jsondata)
#print(type(data1))
headers={
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

a=requests.post(url=url,data=data,headers = headers)
ajson = a.json()
print(ajson)
