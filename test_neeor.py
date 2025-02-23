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

'''
# Apply Gaussian smoothing
sigma = 4  # Standard deviation for smoothing
smoothed_latitude = gaussian_filter1d(latitude, sigma=sigma)
smoothed_longitude = gaussian_filter1d(longitude, sigma=sigma)
smoothed_altitude = gaussian_filter1d(altitude, sigma=sigma)
'''
'''
def exponential_moving_average(data, alpha=0.3):
    smoothed = np.zeros_like(data)
    smoothed[0] = data[0]  # Set initial value
    for i in range(1, len(data)):
        smoothed[i] = alpha * data[i] + (1 - alpha) * smoothed[i - 1]
    return smoothed

# Apply EMA
smoothed_latitude = exponential_moving_average(latitude)
smoothed_longitude = exponential_moving_average(longitude)
smoothed_altitude = exponential_moving_average(altitude)
'''


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
smoothed_latitude = apply_kalman_filter(latitude)
smoothed_longitude = apply_kalman_filter(longitude)
smoothed_altitude = apply_kalman_filter(altitude)


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

