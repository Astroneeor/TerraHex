#functions file
def ggpa(unparsed):
    '''
        splits a $GPGGALONG data into UTC time, latidute and longitude positions 
    '''
    data = unparsed.read().splitlines() #splits data file into a list where each line of data is a row
    final = [] 
    for i in data:        
        body = i.split(',') #splits each row of data into a list
        line = []
        #turns the degree minutes into degrees
        body[1] = int(body[1][0:2]) + float(body[1][2:])/60  
        body[3] = -(int(body[3][0:3]) + float(body[3][3:])/60) 
        #only adds the data we care about
        for j in range(len(body)):
            if j in [0,1,3,8]:
                line.append(body[j])
        final.append(line)
    return final

def filesplit(file):
    lines = file.read().splitlines()
    gppa = open("GGPA.txt",'a')
    sol = open("SOL.txt",'a')
    for line in lines:
        gppa_pot = line.split(',')
        if gppa_pot[0] == "$GPGGA" or gppa_pot[0] == "[USB3]$GPGGA":
            gppa.write(','.join(gppa_pot[1:])+'\n')
        sol_pot = line.split(' ')
        if sol_pot[0] == "<SOL_COMPUTED":
            sol.write(' '.join(sol_pot[1:])+'\n')

def best_pos(unparsed):
    '''
        splits a bestpos abbreviated ascii data into UTC time, latidute and longitude positions 
    '''

    data = unparsed.read().splitlines() #splits data file into a list where each line of data is a row
    final = []
    for i in data:        
        body = i.split(' ') #splits each row of data into a list
        line = []
        #only adds the data we care about
        for j in range(len(body)):
            if j in [1,2,3]:
                line.append(body[j])
        final.append(line)
    return final

def data_to_list(main_data):
    '''
        Takes a list and transposes it
        A column turns into one list in the 2D list

        main_data : 2D list of position data (from any file)
    '''
    singleVarLIst = []
    TransposedList = []
    
    for j in range(len(main_data[0])): # Column of 2D list
        for point in main_data: # Value within dataset
            singleVarLIst.append(point[j])
        TransposedList.append(singleVarLIst)
        singleVarLIst = [] # Reset list after appending
    return TransposedList

if __name__ == "__main__":
    F = open("NewData_3-19.gps",'r')
    print(filesplit(F))
    