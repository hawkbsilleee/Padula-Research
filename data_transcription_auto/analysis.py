from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service
import pandas as pd 

def get_data():
    # returns index of the first empty row in spreadsheet 
    range_name = 'Sheet1!A26:BX1000'
    spreadsheet_id = '1H3SVc9dwfhemI0puZ8-n--FAtWykNH9nzygO2RstrDA'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    return rows

data = {
    "control": {
        "LE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
            "Error White": [],
            "Error Red": [],
            "Error Green": [],
            "Error Blue": [],
        },
        "RE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
            "Error White": [],
            "Error Red": [],
            "Error Green": [],
            "Error Blue": [],
        }
    },
    "experimental": {
        "LE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
            "Error White": [],
            "Error Red": [],
            "Error Green": [],
            "Error Blue": [],
        },
        "RE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
            "Error White": [],
            "Error Red": [],
            "Error Green": [],
            "Error Blue": [],
        }
    }
}

for patient in get_data():
    if patient[-1] == 'Control':
        if patient[2] == 'Left eye':
            index = 59
            for key in data["control"]["LE"]:
                data["control"]["LE"][key].append(patient[index])
                index += 1
        else:
            index = 59
            for key in data["control"]["RE"]:
                data["control"]["RE"][key].append(patient[index])
                index += 1
    if patient[-1] == 'Experimental':
        if patient[2] == 'Left eye':
            index = 59
            for key in data["experimental"]["LE"]:
                data["experimental"]["LE"][key].append(patient[index])
                index += 1
        else:
            index = 59
            for key in data["experimental"]["RE"]:
                data["experimental"]["RE"][key].append(patient[index])
                index += 1

# print(data)
num_patients = len(data["control"]["LE"]["Average White"])

for dictionary in data:
    for eye in data[dictionary]:
        for unaveraged in data[dictionary][eye]:
            lst = [float(num) for num in data[dictionary][eye][unaveraged]]
            data[dictionary][eye][unaveraged] = round(sum(lst)/len(lst),2)

df1 = pd.DataFrame(data["control"])
df2 = pd.DataFrame(data["experimental"])

def extract_num_patients():
    num_experimental = 0
    num_control = 0
    for patient_list in get_data():
        if patient_list[-1] == "Experimental":
            num_experimental += 0.5
        if patient_list[-1] == "Control":
            num_control += 0.5
    num_patients = num_control + num_experimental
    return (num_experimental, num_control, num_patients)

def compare():
    experimental_LE = [value for value in df2['LE']]
    experimental_RE = [value for value in df2['RE']]
    control_LE = [value for value in df1['LE']]
    control_RE = [value for value in df1['RE']]

    comparison_RE = []
    comparison_LE = []
    for i in range(10):
        if experimental_LE[i] > control_LE[i]:
            comparison_LE.append(("experimental", round(abs(experimental_LE[i]-control_LE[i]),2)))
        else: 
            comparison_LE.append(("control", round(abs(experimental_LE[i]-control_LE[i]))))
        if experimental_RE[i] > control_RE[i]:
            comparison_RE.append(("experimental", round(abs(experimental_RE[i]-control_RE[i]))))
        else:
            comparison_RE.append(("control", round(abs(experimental_RE[i]-control_RE[i]))))
    
    # print(f"experimental_LE = {experimental_LE}")
    # print(f"experimental_RE = {experimental_RE}")
    # print(f"control_LE = {control_LE}")
    # print(f"control_RE = {control_RE}")
    # print(comparison_RE)
    # print(comparison_LE)

    comparison =  {
        "LE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
        },
        "RE": {
            "Average White": [],
            "Average Red": [],
            "Average Green": [],
            "Average Blue": [],
            "Area White": [],
            "Area Red": [],
            "Area Green": [],
            "Area Blue": [],
            "Area BS": [], 
        }
    }
    index = 0
    for key in comparison["LE"]:
        comparison["LE"][key].append(comparison_LE[index][0])
        comparison["LE"][key].append(comparison_LE[index][1])
        index += 1
    index = 0 
    for key in comparison["RE"]:
        comparison["RE"][key].append(comparison_RE[index][0])
        comparison["RE"][key].append(comparison_RE[index][1])
        index += 1  

    comparison_df = pd.DataFrame(comparison) 
    
    return comparison_df

def display_data():
    print("\nDATASET ANALYSIS")
    print(f"\nNumber of Total Patients: {int(extract_num_patients()[-1])}")
    print(f"Number of Control: {int(extract_num_patients()[1])}")
    print(f"Number of Experimental: {int(extract_num_patients()[0])}")
    print("\nControl")
    print(df1)
    print("\nExperimental")
    print(df2)
    print("\nCompare")
    print(compare())
    print("\n")

display_data()


