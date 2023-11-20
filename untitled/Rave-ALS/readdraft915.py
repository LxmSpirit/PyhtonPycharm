import xlrd
import os
import re
import jieba
import sys

URL = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/ALS/95.xls'
formaddress = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/formdata6.txt'
fieldaddress = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/fieldata914.txt'
def readforms():
    workbook = xlrd.open_workbook(URL)
    #print(workbook.sheet_names())
    sheet1 = workbook.sheet_by_name('Forms')
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数
    dicform = {}
    for i in range(1,nrows):
        cellOID = sheet1.cell(i,0).value
        cellName = sheet1.cell(i, 2).value
        newOID = re.sub(r'\d+', '', cellOID)
        pattern = re.compile('[!@#$%^&*\(\)（）_+[\]{};:,，./<>?\|`~-]')
        cellName2 = re.sub(pattern, '', cellName)
        newName = jieba.lcut_for_search(cellName2)
        s = ""
        for name in newName:
            s = s + " " + name

        if newOID in dicform:
            oldv = dicform[newOID]
            dicform[newOID] = oldv+" "+ s
        else:
            dicform[newOID] =  s
        #print(cellOID, newOID,cellName,s)
        #print( newOID, s)
    #print(nrows,ncols)
    #print(dicform)
    return dicform

def readfields():
    workbook = xlrd.open_workbook(URL)
    #print(workbook.sheet_names())
    sheet1 = workbook.sheet_by_name('Fields')
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数
    dicfield = {}
    #print(nrows, ncols)
    for i in range(1,nrows):
        formOID = sheet1.cell(i,0).value
        fieldOID = sheet1.cell(i,1).value
        fieldName2 = sheet1.cell(i, 14).value
        pattern = re.compile('[!？@#$%^&*\(\)（）_+[\]{};:,，./<>?\|`~-]')
        fieldName = re.sub(pattern, '', fieldName2)
        if (formOID in fieldOID):
            newfieldOID = fieldOID.replace(formOID,"")
        else :
            newfieldOID = fieldOID

        newName = jieba.lcut_for_search(fieldName)
        s = ""
        for name in newName:
            s = s + " " + name
        if newfieldOID in dicfield:
            oldv = dicfield[newfieldOID]
            dicfield[newfieldOID] = oldv+" "+ s
        else:
            dicfield[newfieldOID] = s
        #print(formOID,fieldOID ,newfieldOID, fieldName)
        #print(nrows, ncols)
        #dicfield[newfieldOID] = fieldName
    return dicfield


def write(data,address):
    file = open(address,mode='w',encoding='utf-8')
    for k,v in data.items():
        file.write(k+'_'+v+'\n')

def coutdic(data):
    keysum = len(data)
    dicv = {}
    onlyv={}
    dick = {}
    maximum = {}
    Prior = {}
    pv = {}
    for k in data:
        #strv = str(v)
        v = data[k]
        vlist = v.split(" ")
        while "" in vlist:
            vlist.remove("")
        for i in vlist:
            str = k+'_'+i
            if str in dicv:
                num = dicv[str]
                dicv[str] = num +1
            else:
                dicv[str] =  1
        if k in dick:
            numk = dick[k]
            dick[k] = numk+1
        else:
            dick[k] =len(vlist)
    #用于计算v
    for k in data:
        #strv = str(v)
        v = data[k]
        vlist = v.split(" ")
        while "" in vlist:
            vlist.remove("")
        for i in vlist:
            if i in onlyv:
                num = onlyv[i]
                onlyv[i] = num +1
            else:
                onlyv[i] =  1

    print("dicv")
    print(dicv)#
    print("dick")
    print(dick)
    print("v")
    print(onlyv)

    sumv = 0

    for a in onlyv:
        sumv = sumv+onlyv[a]

    print("sumv")
    print(sumv)
    #print(keysum)

    for a in onlyv:
        num = onlyv[a] / sumv
        pv[a] = num
    print("pv")
    print(pv)

    for key in dicv:
        n1 = dicv[key]
        k = key.split("_")
        n2 = dick[k[0]]
        res = n1 / n2
        maximum[key] = res

    print("maximum")
    print(maximum)

    sum = 0
    for key in dick:
        n1 = dick[key]
        sum = sum +n1
        #Prior[key] = res
    print("keysum")
    print(sum)

    for key in dick:
        n1 = dick[key]
        res = n1 / sum
        Prior[key] = res

    print("Prior")
    print(Prior)
    return maximum,Prior,pv

def predict(train,str):
    pattern = re.compile('[!@#$%^&*\(\)（）_+[\]{};:,./<>?\|`~-]')
    newstr1 = re.sub(pattern, '', str)
    newstr = jieba.lcut_for_search(newstr1)
    print(newstr)
    res = {}
    for prestr in newstr:
        for k in train:#训练数据集
            k1 = k.split("_")
            key = k1[0]#结果的Key
            if k1[1]==prestr:
                if key in res:#计算结果
                    a = res[key]
                    v = a * train[k]
                    res[key] = v
                else:
                    res[key] = 1*train[k]
    print(res)
    return res

def predict2(pxy,py,px,str):
    pattern = re.compile('[!@#$%^&*\(\)（）_+[\]{};:,./<>?\|`~-]')
    newstr1 = re.sub(pattern, '', str)
    newstr = jieba.lcut_for_search(newstr1)
    print(newstr)
    res = {}

    for prestr in newstr:
        for k in pxy:#训练数据集
            k1 = k.split("_")
            key = k1[0]#结果的Key
            a1 = 0
            a2 = 0
            a3 = 1
            if k1[1]==prestr:
                a1 = pxy[k]
                if k1[1] in px:
                    a3 = px[k1[1]]
                if key in py:
                    a2 = py[key]
                resu = (a1 * a2) / a3
                if key in res:  # 计算结果
                    a = res[key]
                    v = a + resu
                    res[key] = v
                else:
                    res[key] = resu

    print(res)
    return res

def endres(res):
    maxres = -1
    for k in res:
        if res[k]>maxres:
            maxres = res[k]
            resk = k
    if maxres !=-1:
        print(resk)
        return resk
    else:
        print("QAQ")
        return None

def removenull(data):
    for k in data:
        #strv = str(v)
        v = data[k]
        vlist = v.split(" ")
        print(vlist)
        while "" in vlist:
            vlist.remove("")
        print(vlist)
        print("---")

if __name__ == '__main__':
    dicform = readforms()
    print("---readforms---")
    print(dicform)
    #removenull(dicform)
    pxy,py,px = coutdic(dicform)
    print("---coutdic---")
    print(pxy)
    print(py)
    print(px)
    str = "给药记录"
    res = predict2(pxy,py,px, str)
    print("---predict2---")
    print(res)
    #a=endres(res)
    #print(a)

    dicfield = readfields()
    #write(dicfield,fieldaddress)
    pxy1, py1, px1 = coutdic(dicfield)
    str = "其他请详述"
    res = predict2(pxy1, py1, px1, str)
    print("---predict2---field---")
    print(res)
    print("---endres---field---")
    endres(res)

