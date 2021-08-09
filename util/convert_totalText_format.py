'''
This file help to convert format data (4 point) to totalText format(10 point for 1 polygon)
'''
from abc import abstractproperty
import os 
import sys
import glob 
import math 

if len(sys.argv) < 3:
    print("Miss argv")

input_path = sys.argv[1]
output_path = sys.argv[2] 
number_point = 3 # number point you want to interpolate

def interpolate_y(x_1, y_1, x_2, y_2, x):
    '''
    This function interpolate x from strange function(x_1, y_1, x_2, y_2)
    (x - x_1)/(x_2 - x_1) = (y - y_1)/(y_2 - y_1)
    '''
    return ((x-x_1)*(y_2 - y_1)/(x_2 - x_1)) + y_1

def interpolate_x(x_1, y_1, x_2, y_2, y):
    '''
    This function interpolate x from strange function(x_1, y_1, x_2, y_2)
    (x - x_1)/(x_2 - x_1) = (y - y_1)/(y_2 - y_1)
    '''
    return ((y - y_1)*(x_2 - x_1)/(y_2 - y_1)) + x_1

def interpolate_point(num_point, coordinates):
    '''
    coordinates = [x_1, y_1, x_2, y_2]
    '''
    x_1, y_1, x_2, y_2 = coordinates[0],  coordinates[1], coordinates[2],  coordinates[3]
    step = round(abs((x_2 - x_1))/(num_point + 1))
    result = []
    i = 1
    while i <= num_point:
        temp_x =  x_1 + step*i 
        temp_y = interpolate_y(x_1, y_1, x_2, y_2, temp_x)
        result.append(temp_x)
        result.append(temp_y)
        i += 1
    result = [x_1, y_1] + result + [x_2, y_2]
    return result
def preprocessing_line(line):
    line = line.strip('\n')
    if line[-1] == ",":
        line = line[:-1] +  "." 
    split_line = line.split(",") 
    if len(split_line) > 9:
        rec = split_line[8:].replace(",", ".")
        new_line = ""
        for i in range(8):
            new_line += split_line[i] + ","
        new_line = new_line + rec
        line = new_line
    return line

def convert_total_text_format(input_path, output_path):
    for file_name in os.listdir(input_path):
        print("Processing: ", file_name)
        old_path = os.path.join(input_path, file_name)
        new_path = os.path.join(output_path, file_name)

        old_fi = open(old_path, "r") 
        new_fi = open(new_path, "w")

        old_data = old_fi.readlines()
        for line in old_data:
            line = preprocessing_line(line)
            print("line: ", line)
            coordinates = line.split(",")[:-1]
            rec = line.split(",")[-1]
            
            if rec == "###":
                continue
            coordinates = [int(coordinate) for coordinate in coordinates]
            # print("coordinates: ", coordinates)
            # print("rec: ", rec)
            upper_coordinates = interpolate_point(number_point, coordinates[:4])
            lower_coordinates = interpolate_point(number_point, coordinates[4:])
            # print("upper coordinates: ", upper_coordinates)
            # print("lower coordinates: ", lower_coordinates)
            new_coordinates = upper_coordinates + lower_coordinates
            new_annot = "" 
            for coordinate in new_coordinates:
                new_annot += str(round(coordinate)) + ","
            new_annot += rec 
            new_fi.write(new_annot + "\n")
            # print("new annotation: ", new_annot)   
        old_fi.close()
        new_fi.close()
        

convert_total_text_format(input_path, output_path)


'''
CMD
python util/convert_totalText_format.py \
    datasets/VinText/vietnamese/test_labels \
    datasets/VinText/vietnamese/test_new_labels
'''





