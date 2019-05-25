import csv

grip_index = []
grip_data = []

with open('Data/Grip_position.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        multi_sensor_data = []
        temp = row[0]
        splitted_row = temp.split()
        #print(splitted_row)
        data_index = splitted_row[0]
        grip_index.append(data_index)

        for i in range(8):
            sensor_data = splitted_row[i+1].split(':')[1]
            multi_sensor_data.append(sensor_data)
        grip_data.append(multi_sensor_data)
    print(grip_data)
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#           line_count += 1
#        else:
#            print(row)
#            line_count += 1
    print(f'Grip position')

relax_index = []
relax_data = []
with open('Data/Relax_position.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        multi_sensor_data = []
        temp = row[0]
        splitted_row = temp.split()
        #print(splitted_row)
        data_index = splitted_row[0]
        relax_index.append(data_index)

        for i in range(8):
            sensor_data = splitted_row[i+1].split(':')[1]
            multi_sensor_data.append(sensor_data)
        relax_data.append(multi_sensor_data)
    print(relax_data)
    print(f'grip position')