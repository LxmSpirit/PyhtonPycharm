import http.client, urllib.parse
import json

str = json.dumps({"Email":"admin@improve-quality.com","Password":"123456"})
print(str)

# 下面注释部分这样做是不行的
# pararms = urllib.parse.urlencode({'userid':'381fccbd776c4deb'}).encode(encoding='utf8')
headers = {
    "content-type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
conn = http.client.HTTPConnection("192.168.1.144")
conn.request('POST', '/loginApi/User/Login', str, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read().decode('utf-8')
print(data)
print(response)
conn.close()