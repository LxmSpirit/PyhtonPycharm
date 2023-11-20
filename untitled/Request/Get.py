# 导入requests包
import requests

url = "https://www.baidu.com/"
#myParams = {"key": "username", "info": "plusroax"}  # 字典格式，推荐使用，它会自动帮你按照k-v拼接url
res = requests.get(url=url)

print('url:', res.request.url)  # 查看发送的url
print("response:", res.text)  # 返回请求结果
