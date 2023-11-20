import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

print(math.pi)
def drawHeart():
    t = np.linspace(0, 3, 100000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 0.5)
    plt.plot(x, y, color='red', linewidth=10)
    plt.plot(-x, y, color='red', linewidth=10)
    # plt.xlabel('t')
    # plt.ylabel('h')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

    plt.legend()
    plt.show()


drawHeart()
