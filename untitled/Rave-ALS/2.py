import pandas
import numpy as np
dic = {"a": [1, 2, 3, 4], #列表
       "b": np.array([4, 5, 6, 7]), #数组
       "c": (1, 2, 3, 4)} #元组
data = pandas.DataFrame(dic)
print(data[["a","b"]])
print(type(data[["a","b"]]))