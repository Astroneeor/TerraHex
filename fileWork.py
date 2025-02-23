import csv
from fun import *

gpgga = open('data_files/GGPA.txt', 'r')
bestpos = open('data_files/SOL.txt', 'r')
gpgga_list = ggpa(gpgga)
bestpos_list = best_pos(bestpos)

with open('data_files/output_ggpa.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(gpgga_list)

with open('data_files/output_best.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bestpos_list)