from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from fun import *

f = open("SOL.txt",'r')
bestpos = best_pos(f)
data = data_to_list(bestpos)
x_full = data[1]
y_full = data[0]
altitude = data[2]
for i in range(len(x_full)):
    x_full[i] = float(x_full[i])+114
    y_full[i] = float(y_full[i])-51
    altitude[i] = float(altitude[i])
fig = plt.figure(figsize=(7,5))
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
plt.yticks([])

x = []
y = []
print(min(y_full),max(y_full))
colors = []
plt.ylim(0.07876365330000112,0.07946448127999872)
plt.xlim(-0.13189630482000325,-0.1304518726600037)
def animation_func(i):
    x= x_full[i]
    y= y_full[i]
    a = altitude[i]-min(altitude)
    plt.scatter(x, y, c = 255*a/(max(altitude)-min(altitude)), s = 10, alpha = 0.5)

animation = FuncAnimation(fig, animation_func,interval = 0)
plt.show()