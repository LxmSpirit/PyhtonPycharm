import matplotlib.pyplot as plt

year=[1950,1970,1990,2010]

pop=[2.518,3.68,5.23,6.97]
#线
plt.plot(year,pop)
plt.show()
#散点
plt.scatter(year,pop)
plt.show()
#直方图
values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
#有12个数据，bins=3将其分为3段，即(0,2),(2,4),(4,6),从直方图中可以看出(2,4)中的数据最多
plt.hist(values,bins=3)
plt.show()