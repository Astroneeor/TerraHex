csv = open('output_best.csv', 'r')
line = csv.read().splitlines()
for i in range(len(line)):
    line[i] = line[i].split(',')
    line[i] = [float(x) for x in line[i]]

for i in range(0, len(line), 50):
    table_values = open('table_values.csv', 'a')
    table_values.write(str(line[i][0]) + ',' + str(line[i][1]) + ',' + str(line[i][2]) + '\n')