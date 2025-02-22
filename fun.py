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
        body[3] = int(body[3][0:2]) + float(body[3][2:])/60 
        #only adds the data we care about
        for j in range(len(body)):
            if j in [0,1,3,8]:
                line.append(body[j])
        final.append(line)
    return final

def best_pos(unparsed):
    '''
        splits a bestpos abbreviated ascii data into UTC time, latidute and longitude positions 
    '''

    data = unparsed.read().splitlines()#splits data file into a list where each line of data is a row
    final = []
    for i in data:        
        body = i.split(' ')#splits each row of data into a list
        line = []
        #only adds the data we care about
        for j in range(len(body)):
            if j in [1,2,3]:
                line.append(body[j])
        final.append(line)
    return final



if __name__ == "__main__":
    F = open("GGPA.txt",'r')
    print(ggpa(F))
    