import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import pandas as pd
from fileWork import *

# Given data (converted to float)
data = bestpos_list

# Convert to numpy arrays
latitude = np.array([float(d[0]) for d in data])
longitude = np.array([float(d[1]) for d in data])
altitude = np.array([float(d[2]) for d in data])
time = np.arange(len(latitude))  # Time as index

# Apply Gaussian smoothing
sigma = 2  # Standard deviation for smoothing
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

# Display the smoothed data
print("\nSmoothed Coordinate Data:")
print(df_smoothed)

plt.figure(figsize=(8, 6))
plt.plot(smoothed_longitude, smoothed_latitude, marker='o', linestyle='-', color='blue', label="Smoothed Path")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Smoothed Walking Path')
plt.legend()
plt.grid()
plt.show()

# Plot Smoothed Altitude vs Time
plt.figure(figsize=(8, 4))
plt.plot(time, smoothed_altitude, marker='o', linestyle='-', color='red', label="Smoothed Altitude")
plt.xlabel('Time Index')
plt.ylabel('Altitude (meters)')
plt.title('Smoothed Altitude Over Time')
plt.legend()
plt.grid()
plt.show()
