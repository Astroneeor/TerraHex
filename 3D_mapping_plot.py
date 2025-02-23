import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

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

plt.savefig("3D_mapping_plot.png", dpi=600, bbox_inches='tight')
ax.cla()

sigma = 10  # Standard deviation for smoothing
smoothed_latitude_gauss = gaussian_filter1d(x, sigma=sigma)
smoothed_longitude_gauss = gaussian_filter1d(y, sigma=sigma)
smoothed_altitude_gauss = gaussian_filter1d(z, sigma=sigma)

ax.scatter(smoothed_latitude_gauss, smoothed_longitude_gauss, smoothed_altitude_gauss, c = 'r', s = 10)
ax.set_title('Smoothed Path taken while surveying')
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

plt.savefig("3D_mapping_plot_smoothed.png", dpi=600, bbox_inches='tight')
plt.show()

