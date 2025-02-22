# Functions for geomatics math data
# lamba is longitude
# phi is latitude
import math

semimajor = 6378137.0
semiminor = 6356752.314
flattening = 298.257223563
eccentricity = 0.006694

latittude = 0
longitude = 0

def EarthRadius(lat):
    Nfunction = semimajor / (math.sqrt(1-eccentricity*(math.sin(lat)^2)))
    Mfunction = Nfunction * (1-eccentricity) / (math.sqrt(1-eccentricity*(math.sin(lat)^2)))
    return (Nfunction, Mfunction)

def LatToVector(lat, long, alt):
    Xcoord = (EarthRadius(lat)[0] + alt) * math.cos(lat) * math.cos(long)
    Ycoord = (EarthRadius(lat)[0] + alt) * math.cos(lat) * math.sin(long)
    Zcoord = ((1-eccentricity) * EarthRadius(lat)[0] + alt) * math.sin(lat)
    return (Xcoord, Ycoord, Zcoord)

def distance():
    pass