from fun import *
from geomath import *
import math

gpgga = open('GGPA.txt', 'r')
bestpos = open('SOL.txt', 'r')
gpgga_list = ggpa(gpgga)
bestpos_list = best_pos(bestpos)

print(data_to_list(gpgga_list))
