from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from fun import *

f = open("SOL.txt",'r')
bestpos = best_pos(f)
data = data_to_list(bestpos)
x_full = data[0]
y_full = data[1]
colors = []
fig = plt.figure(figsize=(7,5))
plt.xlabel('')
plt.ylabel('')
plt.xticks([51.07888436815,51.07888436815])
plt.yticks([])
x = []
y = []
colors = []
def animation_func(i):
    x.append(x_full[0])
    y.append(y_full[0])
    x_full.pop(0)
    y_full.pop(0)
    colors.append(0)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y),max(y))
    plt.scatter(x, y, c = colors, s = 10, alpha = 0.5)

animation = FuncAnimation(fig, animation_func, 
                          interval = 100)
plt.show()