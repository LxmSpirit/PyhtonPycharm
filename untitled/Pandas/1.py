#coding=utf-8

import pandas as pd

print(pd.__version__)


mydataset={
    'sites':["Google","Runoob","Wiki"],
    'number':[1,2,3]

}

myvar = pd.DataFrame(mydataset)

print(myvar)