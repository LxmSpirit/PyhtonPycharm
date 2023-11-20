# ctrl+alt+L格式化代码
#coding=utf-8
import gzip
import json
import matplotlib.pyplot as plt
from collections import Counter
import copy
import pandas as pd
from itertools import groupby

#resultstr='/reqSummaryData' #用于汇总数据
# 数据路径
path = "C:\\Users\\user\\Desktop\\test11111.chlsj"
with open(path, "r") as f:
    row_data = json.load(f)

class JSON:
    def __init__(self, path):
        self.path = path
        self.all_time = []
        self.avg_time = 0
        self.reqnum = 0
        self.clustering = []

    def setpath(self, path):
        self.path = path
        return self

    def getclustering(self):
        #self.clustering = Counter(self.all_time)#统计数组相同元素个数

        step = 10
        dict1 = {}
        for k, g in groupby(sorted(self.all_time), key=lambda x: x // step):
            str1 = str(k * step)
            str2 = str((k + 1) * step)
            str3 = len(list(g))
            str4 = str1 + "-" + str2
            dict1.update({str4: str3})
            #print('{}-{}: {}'.format(k * step, (k + 1) * step + 1, len(list(g))))
            #print('---')
            #print(dict1)
        self.clustering.append(dict1)
        sum = 0
        for i in dict1:
            a = dict1[i]
            sum = sum +int(a)

        dict2 = {}
        for i in dict1:
            b = dict1[i]
            part = b/sum
            #str0 =  str('{.2%}%'.format(part*100))
            str0 =  '{:.2f}%'.format(part*100)#按百分比展示
            dict2.update({i: str0})

        self.clustering.append(dict2)


        return self


    def setreqnum(self, reqnum):
        self.reqnum = reqnum
        return self

    def getreqnum(self):
        return self.reqnum

    def setalltime(self, alltime):
        self.all_time.append(alltime)
        return self

    def addtime(self, time):
        self.all_time.append(time)
        return self

    def gettime(self):
        return self.all_time


    def getprint(self):
        print(self.path)
        print(self.all_time)
        print(self.avg_time)

    def getpath(self):
        return self.path

    def getavgtime(self):
        sumtime = 0
        i = 0
        for time in self.all_time:
            sumtime = sumtime + time
            i = i + 1
        self.avg_time = sumtime / i

        #if self.path ==resultstr:
            #self.avg_time = self.all_time[0]/self.reqnum

        return self

    def print_obj(obj):
        #打印对象所有属性
        print(obj.__dict__)

    def get_obj(obj):
        #打印对象所有属性

        response = copy.deepcopy(obj.__dict__)
        response.pop('all_time')

        return response



jsonlist = []
pathlist = []

failjsonlist = []
failpathlist = []


sumtime = 0
sumreq = 0
# 读取每一条json数据
for d in row_data:

    if d['response']['status'] == 200:
        if d['path'] in pathlist:
            for zz in jsonlist:
                if zz.path == d['path']:
                    zz.setalltime(d['durations']['total'])
                    zz.reqnum = zz.reqnum + 1
        else:
            pathlist.append(d['path'])
            a = JSON(d['path'])
            a.setalltime(d['durations']['total'])
            a.reqnum = a.reqnum + 1
            jsonlist.append(a)
        sumtime = sumtime + d['durations']['total']
        sumreq = sumreq + 1
    else:
        if d['path'] in failpathlist:
            for zz in failjsonlist:
                if zz.path == d['path']:
                    zz.setalltime(d['durations']['total'])
                    zz.reqnum = zz.reqnum + 1
        else:
            failpathlist.append(d['path'])
            a = JSON(d['path'])
            a.setalltime(d['durations']['total'])
            a.reqnum = a.reqnum + 1
            failjsonlist.append(a)




#print(len(pathlist))
#print(len(jsonlist))
#print(pathlist)
#print(sumtime)
#print(sumreq)
allavgtime = sumtime / sumreq
#print(allavgtime)
#用于汇总数据--不太有用
#a = JSON(resultstr)
#a.setalltime(sumtime)
#a.reqnum = sumreq
#a.getavgtime()
#jsonlist.append(a)

#用于转化为json格式
resjson=[]
for jsontest in jsonlist:
    jsontest.getavgtime()
    jsontest.getclustering()
    #score = pd.Series(jsontest.all_time)
    #se1 = pd.cut(score, bins=3)
    resjson.append(jsontest.get_obj())

failresjson=[]
for failjsontest in failjsonlist:
    failjsontest.getavgtime()
    failresjson.append(failjsontest.get_obj())




data = {
    'total': {
        'avg_time': allavgtime,
        'req_num': sumreq
    },
    'path_lists': resjson,
    'fail_lists':failresjson

}

print("JSON格式##########")
print(json.dumps(data))

if __name__ == "__main__":
    pass
    # file_path  or path
