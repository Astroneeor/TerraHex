import numpy as np
import pandas as pd
from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
from skyfield.api import load

# Example GPS data (Replace with actual data)
data = [
    [51.07946445418, -114.13146131349, '2025-02-22T10:15:00'],
    [51.07945107524, -114.13150189028, '2025-02-22T10:16:00'],
    [51.07942525421, -114.13157915165, '2025-02-22T10:17:00']
]

df = pd.DataFrame(data, columns=["Latitude", "Longitude", "Timestamp"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Function to calculate bearing (direction in degrees)
def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    x = np.sin(dlon) * np.cos(lat2)
    y = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(dlon)
    bearing = np.degrees(np.arctan2(x, y))
    return (bearing + 360) % 360  # Normalize to 0-360 degrees

# Calculate bearing for each point (except last)
df["Bearing"] = [calculate_bearing(df.iloc[i]["Latitude"], df.iloc[i]["Longitude"],
                                   df.iloc[i+1]["Latitude"], df.iloc[i+1]["Longitude"])
                 if i < len(df) - 1 else None for i in range(len(df))]

# Function to get sky data
def get_sky_data(lat, lon, timestamp):
    location = EarthLocation(lat=lat, lon=lon)
    time = Time(timestamp)
    altaz = AltAz(obstime=time, location=location)

    # Get celestial objects
    sun = get_sun(time).transform_to(altaz)

    return {
        "Sun Altitude": sun.alt.degree,
        "Sun Azimuth": sun.az.degree,
    }

# Apply function to each row
df_sky = df.apply(lambda row: get_sky_data(row["Latitude"], row["Longitude"], row["Timestamp"]), axis=1, result_type="expand")

# Merge data
df = pd.concat([df, df_sky], axis=1)

# Load star data using Skyfield
ts = load.timescale()
eph = load('de421.bsp')

def get_constellation(lat, lon, timestamp):
    t = ts.utc(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
    observer = eph['earth'].topos(latitude_degrees=lat, longitude_degrees=lon)
    stars = load('hipparcos')  # Star catalog
    alt, az, d = observer.observe(stars).apparent().altaz()
    
    visible_stars = stars[alt.degrees > 0]  # Filter stars above horizon
    if len(visible_stars) > 0:
        return visible_stars[0].name  # Return the brightest star visible
    return "None"

# Apply constellation function
df["Brightest Star Visible"] = df.apply(lambda row: get_constellation(row["Latitude"], row["Longitude"], row["Timestamp"]), axis=1)

# Display the results
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.expand_frame_repr", False)  # Prevent column wrapping

# Print table
print(df)