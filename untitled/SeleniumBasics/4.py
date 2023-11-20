#coding=utf-8
'''
http://code.t-appagile.com/users/sign_in

http://code.t-appagile.com/users/sign_in

'''

import requests

import json

import string

from bs4 import BeautifulSoup

login = "http://192.168.1.144/userlogin/index"
#http://code.t-appagile.com/users/sign_in
#login = "http://code.t-appagile.com/users/sign_in"
call = "http://192.168.1.144/homepage/index"

headers = {

'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'zh-CN,zh;q=0.9',

'Cache-Control': 'no-cache',

'Content-Length':'57',

'Content-Type': 'application/json;charset=UTF-8',

'SessionID': '',

'Host': '192.168.1.144',

'Origin': 'http://192.168.1.144',

'Proxy-Connection': 'keep-alive',

'Referer': 'http://192.168.1.144/userlogin/index',

#'Upgrade-Insecure-Requests': '1',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',

}

def HttpPost(apiUrl, data):


    try:

        global headers

        r = requests.post(apiUrl, headers=headers, data=data)
        r.encoding = 'utf-8'

        cook = r.request.headers["SessionID"].split('=')

        lowCook = headers["SessionID"].split('=')

        newCook = lowCook[0] + '=' + lowCook[1] + '=' + cook[2]

        headers["SessionID"] = newCook

        print("登陆成功：", newCook)

        return r
    except:
        return


def HttpGet(apiUrl):


    try:

        global headers

        r = requests.get(apiUrl)
        r.encoding='utf-8'

        cook = ""

        for c in r.cookies:

            cook += c.name + "=" + c.value + ";"

        headers["SessionID"] = cook

        print("登陆前的：", cook)

        return r

    except:
        return


def HttpGetLcmm(apiUrl):

    try:

        r = requests.get(apiUrl, headers=headers)
        r.encoding = 'utf-8'

        return r.text

    except:

        return

#res = HttpGet(login)
#print(res)

#html = BeautifulSoup(res, "html.parser")

#token = html.find_all(type="hidden")[1]["value"]
#print(html)

postData = {}

#postData["utf8"] = "✓"

postData["authenticity_token"] = ''

postData["username"] = "admin@improve-quality.com"

postData["password"] = "123456"

res = HttpPost(login, postData)

# print(res.status_code)

print(res)

# print(html)

#res = HttpGetLcmm("http://code.t-appagile.com/SI.Web/lcmm-web")


