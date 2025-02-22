from fun import *
from geomath import *
import math

gpgga = open('GGPA.txt', 'r').read().splitlines()
bestpos = open('bestpos.txt', 'r').read().splitlines()

gpgga_list = ggpa(gpgga)
bestpos_list = best_pos(bestpos)

for i in range(6):
    print(gpgga_list[i])
    print(bestpos_list[i])
