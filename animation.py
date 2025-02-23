from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from fun import *

f = open("GGPA.txt",'r')
ggpa_data = ggpa(f)
data = data_to_list(ggpa_data)
x_full = data[2]
y_full = data[1]
time = data[0]
for i in range(len(time)):
    time[i] = float(time[i])
x_sort = [[data[2][i],time[i]] for i in range(len(data[2]))]
y_sort = [[data[1][i],time[i]] for i in range(len(data[1]))]
x_sort.sort()
y_sort.sort()

def find(thing,xy):
    if xy == 'x':
        for i in range(len(x_sort)):
            if x_sort[i][0] == thing[0] and x_sort[i][1] == thing[1]:
                return i
    elif xy == 'y':
        for i in range(len(y_sort)):
            if y_sort[i][0] == thing[0] and y_sort[i][1] == thing[1]:
                return i
    return 0

for i in range(len(x_full)):
    x_full[i] = float(x_full[i])
    y_full[i] = float(y_full[i])
    time[i] = float(time[i])
fig = plt.figure(figsize=(7,5))
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
plt.yticks([])
color = []
sub = fig.subplots()
x = []
y = []
colors = []
plt.ylim(51.07876365330000112,51.07946448127999872)
plt.xlim(-114.13189630482000325,-114.1304518726600037)
plot = sub.plot([], [], animated=True)[0]
pos_x = 0
def animation_func(i):
    pos_x = find([x_full[i],time[i]],'x')
    pos_y = find([y_full[i],time[i]],'y')
    # print(pos_y,'---------------------------------------------------------------__________________________________________________________')
    x_avg = 0
    y_avg = 0
    for j in [-2,-1,0,1,2]:
        if pos_x+j < len(x_sort) and pos_x+j>=0:
            x_avg+=(x_sort[pos_x+j][0])
        if pos_y+j < len(y_sort) and pos_x+j>=0:
            y_avg+=(y_sort[pos_y+j][0])
    x.append(x_avg/5)
    y.append(y_avg/5)
    color.append(0)
    artist = plt.scatter(x, y, c = color, s = 10, alpha = 0.5)
    return artist,plot

animation = FuncAnimation(fig, animation_func,interval = 0,blit=True,frames=1940)
plt.show()