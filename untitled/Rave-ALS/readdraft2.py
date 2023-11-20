import xlrd
import os
import re
import jieba
#导入数值计算库
import numpy as np
#导入科学计算库
import pandas as pd

#导入GaussianNB库
from sklearn.naive_bayes import GaussianNB

URL = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/ALS/95.xls'
formaddress = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/formdata2.txt'
fieldaddress = 'D:/Work/Python/PycharmProjects/untitled/Rave-ALS/fieldata2.txt'
def readforms():
    workbook = xlrd.open_workbook(URL)
    #print(workbook.sheet_names())
    sheet1 = workbook.sheet_by_name('Forms')
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数
    dicform = {}
    listOID = []
    listName = []
    for i in range(1,nrows):
        cellOID = sheet1.cell(i,0).value
        cellName = sheet1.cell(i, 2).value
        newOID = re.sub(r'\d+', '', cellOID)
        pattern = re.compile('[!@#$%^&*\(\)（）_+[\]{};:,./<>?\|`~-]')
        cellName2 = re.sub(pattern, '', cellName)
        newName = jieba.lcut_for_search(cellName2)
        for name in newName:
            listOID.append(newOID)
            listName.append(name)

        #print(cellOID, newOID,cellName,s)
        #print( newOID, s)
    #print(nrows,ncols)
    #print(dicform)
    #oid = pd.Series(listOID)
    #name = pd.Series(listName)
    return listOID,listName

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
        pattern = re.compile('[!？@#$%^&*\(\)（）_+[\]{};:,./<>?\|`~-]')
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
        file.write(str(k)+'_'+str(v)+'\n')



if __name__ == '__main__':
    oid,form = readforms()
    print(len(oid))
    print(len(form))
    print(oid)
    print(form)
    #write(dicform,formaddress)
    #clf = GaussianNB()
    #dicfield = readfields()

    #clf.fit(form, oid)
    #GaussianNB(priors=None)
    #clf.predict(["访视"])
    #write(dicfield,fieldaddress)