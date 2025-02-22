#functions file
def ggpa(unparsed):
    '''
        splits an ascii $GPGGALONG into UTC time, latidute and longitude position and direction, 
        and time between measurements
    '''
    body = unparsed.split(',')
    final = []
    body[1] = int(body[1][0:2]) + float(body[1][2:])/60 
    body[3] = int(body[3][0:2]) + float(body[3][2:])/60 
    for i in range(len(body)):
        if i in [0,1,2,3,4,8]:
            final.append(body[i])
    return final

def best_pos(unparsed):
    body = unparsed.split(',')
    final = []
    for i in range(len(body)):
        if i in [1,2,3]:
            final.append(body[i])
    return final

def plot():
    pass

def path_smoothing():
    pass

if __name__ == "__main__":
    F = open("GGPA.txt",'r')
    data = F.read().splitlines()
    for i in data:
        print(best_pos(i))