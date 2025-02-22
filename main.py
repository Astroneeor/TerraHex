from fun import *
from geomath import *
import math

gpgga = open('GGPA.txt', 'r')
bestpos = open('SOL.txt', 'r')
gpgga_list = ggpa(gpgga)
bestpos_list = best_pos(bestpos)

def data_to_list(main_data):
    '''
        Takes a list and transposes it
        A column turns into one list in the 2D list

        main_data : 2D list of position data (from any file)
    '''
    singleVarLIst = []
    TransposedList = []
    for j in range(len(main_data[0])):
        for point in main_data:
            singleVarLIst.append(point[j])
        TransposedList.append(singleVarLIst)
        singleVarLIst = []
    return TransposedList

print(data_to_list(gpgga_list))
