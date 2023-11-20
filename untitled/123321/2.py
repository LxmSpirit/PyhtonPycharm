import time
import matplotlib.pyplot as plt
import numpy as np
import math

def pow(x,a):
    return math.pow(x,a)

plt.ion()
figure,ax=plt.subplots()
lines,=ax.plot([],[],color="red")
ax.set_autoscaley_on(True)
ax.grid()
X=np.linspace(-1.8,1.8,1000)
a=1

while True:
	#设置函数
    y = [pow(pow(x, 2), 1 / 3) + 0.9 * pow(3.3 - x * x, 0.5) * np.sin(a * np.pi * x) for x in X]
    a=a+0.1
    lines.set_xdata(X)
    lines.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.01)
