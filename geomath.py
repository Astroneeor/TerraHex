# Functions for geomatics math data
# lamba is longitude
# phi is latitude
from math import cos, sin, sqrt

semimajor = 6378137.0
semiminor = 6356752.314
flattening = 298.257223563
eccentricity = 0.006694

data_sample = [['time', 'long', 'lat', 'alt'], ['time1', 'long2', 'lat3', 'alt']]

def EarthRadius(lat):
    Nfunction = semimajor / (sqrt(1-eccentricity*(sin(lat)^2)))
    Mfunction = Nfunction * (1-eccentricity) / (sqrt(1-eccentricity*(sin(lat)^2)))
    return (Nfunction, Mfunction)

def LatToVector(lat, long, alt):
    Nfunction = EarthRadius(lat)[0]
    Xcoord = ( Nfunction + alt) * cos(lat) * cos(long)
    Ycoord = (Nfunction + alt) * cos(lat) * sin(long)
    Zcoord = ((1-eccentricity) * Nfunction + alt) * sin(lat)
    return (Xcoord, Ycoord, Zcoord)

def LatToENU(lat_i, long_i, alt_i, lat, long, alt):
    Nfunction = EarthRadius(lat)[0]
    Mfunction = EarthRadius(lat)[1]

    East = (Nfunction + alt) * cos(lat) * (long-long_i)
    North = (Nfunction + alt) * (lat-lat_i)
    Uptick = (alt - alt_i)

    return (East, North, Uptick)
    