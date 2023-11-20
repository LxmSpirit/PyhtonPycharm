import requests
import xlwt
import xlrd
import json
from xlutils import copy
import random
import string
import browser_cookie3



dict1 = browser_cookie3.chrome(domain_name='www.cde.org.cn')
Cookies=""
for u in dict1:
    Cookies =Cookies+""+u.name+"="+u.value+"; "
#print("Cookies:",Cookies)


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
    res2 = res.text
    new_dic2 = json.loads(res2)
    resdata = new_dic2.get("data")
    respages = resdata.get("pages")
    allpages = respages+1


    for ii in range(1,allpages):

        data = {"pageSize": 1000, "pageNum": ii}
        res = requests.post(url=url, data=data, headers=headers)

        res2 = res.text
        new_dic2 = json.loads(res2)
        resdata = new_dic2.get("data")
        resrecords = resdata.get("records")  # list
        aa = len(resrecords)

        star = lenn
        print(lenn)
        for i in range(0, aa):
            data = resrecords[i]
            j = 0
            star = star+1
            for k, v in data.items():
                wsheet.write(star, j, v)
                j = j + 1

        lenn = lenn + aa


    wbook.save(savepath)




# 调用
get_data()
