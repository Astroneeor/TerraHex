import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import pandas as pd
from fileWork import *
import folium

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

# Create a dataframe to display
df_smoothed = pd.DataFrame({
    'Time Index': time,
    'Smoothed Latitude': smoothed_latitude,
    'Smoothed Longitude': smoothed_longitude,
    'Smoothed Altitude': smoothed_altitude
})


# Create a Folium map centered at the first coordinate
map_center = [smoothed_latitude[0], smoothed_longitude[0]]
m = folium.Map(location=map_center, zoom_start=17)

# Add the smoothed walking path to the map
path = list(zip(smoothed_latitude, smoothed_longitude))
folium.PolyLine(path, color="blue", weight=4.5, opacity=0.8).add_to(m)

# Add markers for start and end points
folium.Marker(path[0], popup="Start", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(path[-1], popup="End", icon=folium.Icon(color="red")).add_to(m)

# Save and display the map
map_filename = "smoothed_walking_path.html"  # Saves in the same directory as your script
m.save(map_filename)
map_filename
