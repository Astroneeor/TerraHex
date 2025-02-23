import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import pandas as pd
from fileWork import *

# Given data (converted to float)
data = bestpos_list

# Setting plot variables
plt.figure(figsize=(8, 6))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid()

# Convert to numpy arrays
latitude = np.array([float(d[0]) for d in data])
longitude = np.array([float(d[1]) for d in data])
altitude = np.array([float(d[2]) for d in data])
time = np.arange(len(latitude))  # Time as index


# Apply Gaussian smoothing
sigma = 4  # Standard deviation for smoothing
smoothed_latitude_gauss = gaussian_filter1d(latitude, sigma=sigma)
smoothed_longitude_gauss = gaussian_filter1d(longitude, sigma=sigma)
smoothed_altitude_gauss = gaussian_filter1d(altitude, sigma=sigma)

plt.title('Gaussian Smoothed Walking Path')
plt.plot(smoothed_longitude_gauss, smoothed_latitude_gauss, marker='o', linestyle='-', color='green', label="Smoothed Path")
plt.savefig("gaussian_smoothed_path.png", dpi=600, bbox_inches='tight')

#Exponential Moving Average smoothing
def exponential_moving_average(data, alpha=0.3):
    smoothed = np.zeros_like(data)
    smoothed[0] = data[0]  # Set initial value
    for i in range(1, len(data)):
        smoothed[i] = alpha * data[i] + (1 - alpha) * smoothed[i - 1]
    return smoothed

# Apply Exponential Moving Average smoothing
smoothed_latitude_ema = exponential_moving_average(latitude)
smoothed_longitude_ema = exponential_moving_average(longitude)
smoothed_altitude_ema = exponential_moving_average(altitude)

plt.title('Exponential Moving Average Smoothed Walking Path')
plt.plot(smoothed_longitude_ema, smoothed_latitude_ema, marker='o', linestyle='-', color='green', label="Smoothed Path")
plt.savefig("ema_smoothed_path.png", dpi=600, bbox_inches='tight')

#Kalman Filter Smothing
from filterpy.kalman import KalmanFilter

def apply_kalman_filter(data):
    kf = KalmanFilter(dim_x=1, dim_z=1)
    kf.x = np.array([[data[0]]])  # Initial state
    kf.F = np.array([[1]])  # State transition matrix
    kf.H = np.array([[1]])  # Measurement function
    kf.P *= 1000  # High initial uncertainty
    kf.R = 10  # Measurement noise
    kf.Q = 1  # Process noise

    smoothed_data = []
    for z in data:
        kf.predict()
        kf.update(z)
        smoothed_data.append(kf.x[0, 0])

    return np.array(smoothed_data)

# Apply Kalman Filter
smoothed_latitude_kf = apply_kalman_filter(latitude)
smoothed_longitude_kf = apply_kalman_filter(longitude)
smoothed_altitude_kf = apply_kalman_filter(altitude)

plt.title('Kalman Filter Smoothed Walking Path')
plt.plot(smoothed_longitude_kf, smoothed_latitude_kf, marker='o', linestyle='-', color='blue', label="Smoothed Path")
plt.savefig("kalman_smoothed_path.png", dpi=600, bbox_inches='tight')  

