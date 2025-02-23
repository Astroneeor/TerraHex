import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

csv = open('output_best.csv', 'r')
line = csv.read().splitlines()
for i in range(len(line)):
    line[i] = line[i].split(',')
    line[i] = [float(x) for x in line[i]]

x = [line[i][1] for i in range(len(line))]
y = [line[i][0] for i in range(len(line))]
z = [line[i][2] for i in range(len(line))]
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.grid()

ax.scatter(x, y, z, c = 'r', s = 10)
ax.set_title('Path taken while surveying')
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
plt.show()