import csv
from fun import *

gpgga = open('GGPA.txt', 'r')
bestpos = open('SOL.txt', 'r')
gpgga_list = ggpa(gpgga)
bestpos_list = best_pos(bestpos)

with open('output_ggpa.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(gpgga_list)

with open('output_best.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bestpos_list)