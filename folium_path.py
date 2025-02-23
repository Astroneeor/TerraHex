### THIS FILE USES FOLIUM TO 
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from fileWork import *
import folium

data = bestpos_list

# Setting variabels from the data
latitude = np.array([float(d[0]) for d in data])
longitude = np.array([float(d[1]) for d in data])
altitude = np.array([float(d[2]) for d in data])
time = np.arange(len(latitude))  # Time is used to determine which points are being used

# Applying smoothing using the gaussian filter
sigma = 4  # Standard deviation for smoothing
smoothed_latitude = gaussian_filter1d(latitude, sigma=sigma)
smoothed_longitude = gaussian_filter1d(longitude, sigma=sigma)
smoothed_altitude = gaussian_filter1d(altitude, sigma=sigma)

# Folium map is centered around the first point, but the website is dynamic and can be navigates
map_center = [smoothed_latitude[0], smoothed_longitude[0]]
m = folium.Map(location=map_center, zoom_start=17)

# Adding the smoothed path to the above map
path = list(zip(smoothed_latitude, smoothed_longitude))
folium.PolyLine(path, color="blue", weight=4.5, opacity=0.8).add_to(m)

# Start and stop icon for your convenience
folium.Marker(path[0], popup="Start", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(path[-1], popup="End", icon=folium.Icon(color="red")).add_to(m)

# Save and display the map as an HTML, which can be accessed by the website
map_filename = "smoothed_walking_path.html"
m.save(map_filename)
