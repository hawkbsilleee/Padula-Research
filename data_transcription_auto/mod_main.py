from update import write_range,  find_empty
from reader import data_extract, mod_data_extract
import os 
import glob

def convert_data(eye, data_dict):
    if eye == 'r':
        values_list_1 = [data_dict['Patient'], '', 'Right eye']
        dict_eye = "RightEye"
    if eye == 'l':
        values_list_1 = [data_dict['Patient'], '', 'Left eye']
        dict_eye = "LeftEye"
    for i in range(12):
        white = data_dict[dict_eye]["Form"][i]
        red = data_dict[dict_eye]["Red"][i]
        green = data_dict[dict_eye]["Green"][i]
        blue = data_dict[dict_eye]["Blue"][i]
        values_list_1.append(white)
        values_list_1.append(red)
        values_list_1.append(green)
        values_list_1.append(blue)
    # Blind spots 
    for index in range(len(data_dict[dict_eye]["BS"])-1):
        values_list_1.append(data_dict[dict_eye]["BS"][index])
    # Averages
    i = 12
    white = data_dict[dict_eye]["Form"][i]
    red = data_dict[dict_eye]["Red"][i]
    green = data_dict[dict_eye]["Green"][i]
    blue = data_dict[dict_eye]["Blue"][i]
    values_list_1.append(white)
    values_list_1.append(red)
    values_list_1.append(green)
    values_list_1.append(blue)
    # Area
    i = -1
    white = data_dict[dict_eye]["Form"][i]
    red = data_dict[dict_eye]["Red"][i]
    green = data_dict[dict_eye]["Green"][i]
    blue = data_dict[dict_eye]["Blue"][i]
    bs = data_dict[dict_eye]["BS"][i]
    values_list_1.append(white)
    values_list_1.append(red)
    values_list_1.append(green)
    values_list_1.append(blue)
    values_list_1.append(bs)
    # Error 
    for value in data_dict[dict_eye]["Error"]:
        values_list_1.append(value)
    values_list_1.append(data_dict['Date'])
    values_list_1.append(data_dict['DOB'])
    return values_list_1

def insert_data(path):    
    data_dict = data_extract(path)
    # convert data_dict into list
    values = []

    values.append(convert_data('r', data_dict))
    values.append(convert_data('l', data_dict))

    values[0].append(path)
    values[1].append(path)

    start_row = find_empty() + 1
    end_row = start_row + 2
    range_name = 'Sheet1!A'+str(start_row)+':BW'+str(end_row)
    write_range(range_name, values)

# for filepath in glob.iglob('pdfs' + '/' + '*'):
#     insert_data(filepath)

