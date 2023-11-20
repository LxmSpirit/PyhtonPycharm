import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
import json
from xlutils import copy
import random
import string
import browser_cookie3

dict1 = browser_cookie3.chrome(domain_name='www.cde.org.cn')
print(dict1)
Cookies=""
for u in dict1:
    Cookies =Cookies+""+u.name+"="+u.value+"; "
#s = ("Cookie: "+s)
print(Cookies)

# 请求headers 模拟谷歌浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}


def get_data():
    value = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    savepath = 'D:/临床试验默示许可'+value+'.xls'
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('临床试验默示许可', cell_overwrite_ok=True)
    col = ('受理号', '药品名称', '申请人名称', '适应症', '注册分类')
    for i in range(0, 5):
        sheet.write(0, i, col[i])
    book.save(savepath)

    xls = xlrd.open_workbook(savepath, formatting_info=True)  # 得到文件
    wbook = copy.copy(xls)  # 复制文件并保留格式
    wsheet = wbook.get_sheet(0)

    url = "https://www.cde.org.cn/main/xxgk/getCliniCalList"
    """
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "FSSBBIl1UgzbN7N80S=dGhwZ1GfWuJPCCmBpU_D5NS72lfleWEO6lNrgxUgoO8uk0dKfSPvd1RlryqGqKqC; FSSBBIl1UgzbN7N80T=3U479HR8h.2LmWmwC.Xgw1WkdtSwNau2KvPs6leJbGYQj0ZYCHMIdXtEu1yH9HRKf1ZHk8SVKsQ.O5XOObtMnA1MkevOoTlAaM8j81mfU4f2gRTb0SMEDJFqFIqxDyZV4tpre3hzHj31Swl8SnDgSDty4UCAHmXivpk_j3NPBGRweA4FthshjNrEpohEPKym9X6_gzhzIx1gY6VT1SyjfhRoWsousrjLfwJZarcBL8SpfVDMBb4NFCRyp5ivjlzDrB6ZfhEQtqC9ywuQ4retEq.QJ3iftZQI2A5Sox9dEFsby9g.SBUPKMxP58IKzTxdukzQ",
        "X-Requested-With": "XMLHttpRequest"
    }
    """
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": Cookies,
        "X-Requested-With": "XMLHttpRequest"
    }
    lenn = 0
    star = 0

    data = {"pageSize": 1000, "pageNum": 1}
    res = requests.post(url=url, data=data, headers=headers)
    #print(res)
    res2 = res.text
    #print(res2)
    new_dic2 = json.loads(res2)
    resdata = new_dic2.get("data")
    respages = resdata.get("pages")
    print('respages', type(respages))
    print('respages',respages)
    allpages = respages+1
    print('allpages', allpages)

    for ii in range(1,allpages):


        # data = {"MmEwMD": "3odz9IwIh4fNmQrQC4jywcEcdFTQNG69K6b16VyWbapwj9gVCII8d5ixucei9IwUfcgikiTYKk3jOXjPOCiFnqKFkdskV1hRcv39Q.pFBEiKylZSQfwji3SBLdK1TOTsJVpmnY2NnWab.Pslaqwd0uH8rSO29z7Om.h0DhD4b9X.8s0GudjL_A3LTWYTeUKjVfb8.49db5z0Bb9LCqwmqMen_eHy_TDviIlqHqbhK5CJCSpgWBqgE0eDmQsQcLdj6T7FeJO1xmjCiVURhmLXFiF9syekq7dZPtqru9T4qpZxwJemQWYtelj40Xg9CirvNoJaFqcKWRfeegM2vYqjnakJMWtNf85TqPMXLMbOLmFECfi4czDTPuXkxbP4kNI5S6oK"}  # Post请求发送的数据，字典格式
        data = {"pageSize": 1000, "pageNum": ii}

        res = requests.post(url=url, data=data, headers=headers)  # 这里传入的data,是body里面的数据。params是拼接url时的参数

        print("发送的body:", res.request.body)
        print("response返回结果：", res.text)
        # selector = etree.HTML(res.text)

        res2 = res.text
        print("res2：", type(res2))
        new_dic2 = json.loads(res2)
        print("new_dic2：", new_dic2)
        resdata = new_dic2.get("data")
        print("resdata：", resdata)
        print("resdata：", type(resdata))
        resrecords = resdata.get("records")  # list
        print("resrecords：", resrecords)
        print("resrecords：", type(resrecords))

        aa = len(resrecords)

        print(len(resrecords))
        a = resrecords[0]
        print("a：", type(a))

        print("@@@@@@@@")


        star = lenn
        print(lenn)
        for i in range(0, aa):
            data = resrecords[i]
            j = 0
            star = star+1
            for k, v in data.items():
                #print(v)
                #sheet.write(lenn + 1, j, v)
                wsheet.write(star, j, v)
                j = j + 1

        lenn = lenn + aa
        #book.save(savepath)
    #savepath = 'D:/临床试验默示许可4.xls'
    #book.save(savepath)
    wbook.save(savepath)


#print("全部完成")

# 调用
get_data()
