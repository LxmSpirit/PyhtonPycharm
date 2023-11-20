# 导入requests包
import requests

url = "http://192.168.1.144/loginApi/User/Login"
data = {"Email":"admin@improve-quality.com","Password":"123456"}  # Post请求发送的数据，字典格式
headers={
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

res = requests.post(url=url, json=data,headers=headers)  # 这里传入的data,是body里面的数据。params是拼接url时的参数

print("发送的body:", res.request.body)
print("response返回结果：", res.text)
