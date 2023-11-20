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
    dick = {}
    maximum = {}
    Prior = {}
    for k in data:
        #strv = str(v)
        v = data[k]
        vlist = v.split(" ")
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
    print(dicv)#
    print(dick)
    #print(keysum)

    for key in dicv:
        n1 = dicv[key]
        k = key.split("_")
        n2 = dick[k[0]]
        res = n1 / n2
        maximum[key] = res

    print(maximum)

    for key in dick:
        n1 = dick[key]
        res = 1 / keysum
        Prior[key] = res

    #print(Prior)
    return maximum

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

def predict2(train,str):
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
                    res[key] = train[k]
    print(res)
    return res

def endres(res):
    min = sys.maxsize
    print(min)
    for k in res:
        if res[k]<min:
            min = res[k]
            resk = k
    if min !=sys.maxsize:
        #print(resk)
        return resk
    else:
        #print("QAQ")
        return None


if __name__ == '__main__':
    dicform = readforms()
    restrain = coutdic(dicform)
    print(restrain)
    str = "步行试验"
    res = predict(restrain, str)
    print("----")
    print(res)
    a=endres(res)
    print(a)


    #write(dicform,formaddress)
    dicfield = readfields()
    write(dicfield,fieldaddress)
    restrain = coutdic(dicfield)
    str = "其他请详述"
    res = predict(restrain, str)
    a=endres(res)
    print(a)