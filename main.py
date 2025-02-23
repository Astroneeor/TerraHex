### We have a lot of files but this was basically the bouler plate for how we figured out the data, using the functions for data parsing, and plotting the data. More of a testing ground for the data. ###

from fileWork import gpgga_list, bestpos_list
import matplotlib.pyplot as plt
from fun import *

f = open("data_files/SOL.txt",'r')
bestpos = best_pos(f)
data = data_to_list(bestpos)
x_full = data[1]
y_full = data[0]
for i in range(len(x_full)):
    x_full[i] = float(x_full[i])-51
    y_full[i] = float(y_full[i])+114
plt.plot(x_full,y_full)
plt.xlim(min(x_full),max(x_full))
plt.ylim(min(y_full),max(y_full))
plt.show()