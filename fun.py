#functions file
def ggpa(unparsed):
    '''
        splits an ascii $GPGGALONG into UTC time, latidute and longitude position and direction, 
        and time between measurements
    '''
    data = unparsed.read().splitlines()
    final = []
    for i in data:        
        body = i.split(',')
        line = []
        body[1] = int(body[1][0:2]) + float(body[1][2:])/60 
        body[3] = int(body[3][0:2]) + float(body[3][2:])/60 
        for j in range(len(body)):
            if j in [0,1,3,8]:
                line.append(body[j])
        final.append(line)
    return final

def best_pos(unparsed):
    data = unparsed.read().splitlines()
    final = []
    for i in data:        
        body = i.split(' ')
        line = []
        for j in range(len(body)):
            if j in [1,2,3]:
                line.append(body[j])
        final.append(line)
    return final



if __name__ == "__main__":
    F = open("GGPA.txt",'r')
    print(ggpa(F))
    