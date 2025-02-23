from fileWork import gpgga_list, bestpos_list
from geomath import *
import matplotlib.pyplot as plt
import math
from fun import *

f = open("SOL.txt",'r')
bestpos = best_pos(f)
data = data_to_list(bestpos)
x_full = data[1]
y_full = data[0]
for i in range(len(x_full)):
    x_full[i] = float(x_full[i])-51
    y_full[i] = float(y_full[i])+114
plt.scatter(x_full,y_full)
plt.xlim(min(x_full),max(x_full))
plt.ylim(min(y_full),max(y_full))
plt.show()