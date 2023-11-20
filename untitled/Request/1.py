#conding=utf-8

import requests
import json

url="http://192.168.1.144/loginApi/User/Login"
data={
	"Email": "admin@improve-quality.com",
	"Password": "123456"
}
data1 = {"Email":"admin@improve-quality.com","Password":"123456"}
jsondata = json.dumps(data1)
print(jsondata)
print(type(jsondata))
print(type(data1))
headers={
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

a=requests.post(url=url,data=data,headers = headers)
ajson = a.json()
print(ajson)
