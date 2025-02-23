import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import pandas as pd
from matplotlib.animation import FuncAnimation
from fileWork import *

# Given data (converted to float)
data = bestpos_list

# Convert to numpy arrays
latitude = np.array([float(d[0]) for d in data])
longitude = np.array([float(d[1]) for d in data])
altitude = np.array([float(d[2]) for d in data])
time = np.arange(len(latitude))  # Time as index

# Apply Gaussian smoothing
sigma = 4  # Standard deviation for smoothing
smoothed_latitude = gaussian_filter1d(latitude, sigma=sigma)
smoothed_longitude = gaussian_filter1d(longitude, sigma=sigma)
smoothed_altitude = gaussian_filter1d(altitude, sigma=sigma)




fig = plt.figure(figsize=(7,5))
plt.title('Smoothed Walking Path')
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
plt.yticks([])
color = []
sub = fig.subplots()
x = []
y = []
plt.ylim(51.07876365330000112,51.07946448127999872)
plt.xlim(-114.13189630482000325,-114.1304518726600037)
plot = sub.plot([], [], animated=True)[0]
def animation_func(i):
    x.append(smoothed_longitude[i])
    y.append(smoothed_latitude[i])
    color.append(0)
    artist = plt.scatter(x, y, marker='o', linestyle='-', color='black', label="Smoothed Path", s=10)
    return artist,plot

interval = 100 # set to 0 for max speed, set to 100 for real time speed
animation = FuncAnimation(fig, animation_func,interval = interval,blit=True,frames=1940)
plt.show()