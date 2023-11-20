# ctrl+alt+L格式化代码
#coding=utf-8
import gzip
import json
import matplotlib.pyplot as plt
from collections import Counter
import copy

resultstr='/reqSummaryData' #用于汇总数据
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
        self.clustering = Counter(self.all_time)#统计数组相同元素个数
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

        if self.path ==resultstr:
            self.avg_time = self.all_time[0]/self.reqnum

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


sumtime = 0
sumreq = 0
# 读取每一条json数据
for d in row_data:

    if d['path'] in pathlist:
        for zz in jsonlist:
            if zz.path == d['path']:
                zz.setalltime(d['durations']['total'])
                zz.reqnum = zz.reqnum +1
    else:
        pathlist.append(d['path'])
        a = JSON(d['path'])
        a.setalltime(d['durations']['total'])
        a.reqnum = a.reqnum + 1
        jsonlist.append(a)
    sumtime = sumtime + d['durations']['total']
    sumreq = sumreq +1

#print(len(pathlist))
#print(len(jsonlist))
#print(pathlist)
#print(sumtime)
#print(sumreq)
allavgtime = sumtime / sumreq
#print(allavgtime)
#用于汇总数据--不太有用
a = JSON(resultstr)
a.setalltime(sumtime)
a.reqnum = sumreq
a.getavgtime()
#jsonlist.append(a)

#用于转化为json格式
resjson=[]
for jsontest in jsonlist:
    jsontest.getavgtime()
    jsontest.getclustering()
    resjson.append(jsontest.get_obj())

data = {
    'total': {
        'avg_time': allavgtime,
        'req_num': sumreq
    },
    'path_lists': resjson,
    'fail_lists':[]

}

print("JSON格式##########")
print(json.dumps(data))

