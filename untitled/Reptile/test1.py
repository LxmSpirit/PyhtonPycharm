#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

#f = open('C:/Users/LP/Desktop/doupo.txt','a+')		#新建txt文档，追加的方式

url = 'http://www.doupoxs.com/doupocangqiong/2.html'
res = requests.get(url,headers = headers)
res1 = res.content.decode('utf-8')
print(res1)
contents =re.findall('<p>(.*?)</p>',res1,re.S)
print(contents)
print(type(contents))
f = open('doupo.txt','a',encoding='utf-8')
for content in contents:
    print(content)
    print(type(content))
    f.write(content+'\n')
    #f.write(str(content))
f.close()


