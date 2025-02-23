from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from fun import *

f = open("GGPA.txt",'r')
data = np.array(ggpa(f),float)

def point_distance(index):
    dist_list = []
    for i in range(len(data)):
        distance = (data[index][0]-data[i][0])**2 + (data[index][1]-data[i][1])**2
        dist_list.append([distance,i])
    dist_list.sort()
    return dist_list

fig = plt.figure(figsize=(7,5))
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
sub = fig.subplots()
x = []
y = []
color = []
plt.ylim(51.07876365330000112,51.07946448127999872)
plt.xlim(-114.13189630482000325,-114.1304518726600037)
plot = sub.plot([], [], animated=True)[0]
pos_x = 0

def animation_func(i):
    distance = point_distance(i)
    x_avg,y_avg = [0,0]
    for j in range(10):
        x_avg += data[distance[j][1]][2]
        y_avg += data[distance[j][1]][1]
    x_avg/=10
    y_avg/=10
    print(x_avg,y_avg)
    x.append(x_avg)
    y.append(y_avg)
    color.append(0)
    artist = plt.scatter(x, y, c = color, s = 20, alpha = 0.5)
    return artist,plot

animation = FuncAnimation(fig, animation_func,interval = 1,blit=True,frames=1940)
plt.show()