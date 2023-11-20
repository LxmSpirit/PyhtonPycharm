import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
import json
from xlutils import copy
import random
import string

# 请求headers 模拟谷歌浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def get_data():
    value = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    savepath = 'D:/临床试验默示许可' + value + '.xls'
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
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "FSSBBIl1UgzbN7N80S=dGhwZ1GfWuJPCCmBpU_D5NS72lfleWEO6lNrgxUgoO8uk0dKfSPvd1RlryqGqKqC; FSSBBIl1UgzbN7N80T=3U479HR8h.2LmWmwC.Xgw1WkdtSwNau2KvPs6leJbGYQj0ZYCHMIdXtEu1yH9HRKf1ZHk8SVKsQ.O5XOObtMnA1MkevOoTlAaM8j81mfU4f2gRTb0SMEDJFqFIqxDyZV4tpre3hzHj31Swl8SnDgSDty4UCAHmXivpk_j3NPBGRweA4FthshjNrEpohEPKym9X6_gzhzIx1gY6VT1SyjfhRoWsousrjLfwJZarcBL8SpfVDMBb4NFCRyp5ivjlzDrB6ZfhEQtqC9ywuQ4retEq.QJ3iftZQI2A5Sox9dEFsby9g.SBUPKMxP58IKzTxdukzQ",
        "X-Requested-With": "XMLHttpRequest"
    }
    lenn = 0
    star = 0


    data = {"pageSize": 1000, "pageNum": 0}

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
        star = star + 1
        for k, v in data.items():
            # print(v)
            # sheet.write(lenn + 1, j, v)
            wsheet.write(star, j, v)
            j = j + 1

    lenn = lenn + aa
    # book.save(savepath)


# savepath = 'D:/临床试验默示许可4.xls'
# book.save(savepath)


# 调用
get_data()
