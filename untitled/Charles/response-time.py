# ctrl+alt+L格式化代码
import gzip
import json
import matplotlib.pyplot as plt


class JSON:
    def __init__(self, path):
        self.path = path
        self.all_time = []
        self.avg_time = 0

    def setpath(self, path):
        self.path = path
        return self

    def setalltime(self, alltime):
        self.all_time.append(alltime)
        return self

    def addtime(self, time):
        self.all_time.append(time)
        return self

    def gettime(self):
        return self.all_time

    def get(self):
        return self.path, self.all_time, self.avg_time

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
        return self


class VisualArray():
    """动态可视化数组"""


    def __init__(self):
        """初始化"""
        self.fig, self.ax = plt.subplots()


    def draw(self, arrays=[], rwidth=0.8, color='black', time=0.0001):
        """
        生成一帧图像
        arrays: 需要显示的数组
        rwidth: 直方图中的条宽
        color: 直方图的颜色
        time: 延迟，默认为0.1ms
        axis: 是否显示坐标轴
        """
        self.ax.cla()  # 清除上一帧图像
        self.ax.bar(range(0, len(arrays)), height=arrays, width=rwidth, color=color)
        plt.pause(time)  # 暂停，防止速度太快无法

    def stop(self):
        """结束绘画，使图片保留在最后一帧"""
        plt.show()


jsonlist = []
pathlist = []

# 数据路径
path = "C:\\Users\\user\\Desktop\\test11111.chlsj"
with open(path, "r") as f:
    row_data = json.load(f)

# 读取每一条json数据
for d in row_data:

    if d['path'] in pathlist:
        for zz in jsonlist:
            if zz.path == d['path']:
                zz.setalltime(d['durations']['total'])
    else:
        pathlist.append(d['path'])
        a = JSON(d['path'])
        a.setalltime(d['durations']['total'])
        jsonlist.append(a)

print(len(pathlist))
print(len(jsonlist))

print(pathlist)

for jsontest in jsonlist:
    jsontest.getavgtime()
    jsontest.getprint()
    print(jsontest.all_time)
    cc = VisualArray()
    cc.draw(jsontest.all_time)
