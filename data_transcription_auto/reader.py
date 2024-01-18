import pdfplumber
import pandas as pd 

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def data_extract(path):

    patient_data = {
    "Patient": None,
    "DOB": None,
    "Date": None,
    "RightEye": {
        "Form": [],
        "Red": [],
        "Green": [],
        "Blue": [],
        "BS": [],
        "Error": [],
    }, 
    "LeftEye": {
        "Form": [],
        "Red": [],
        "Green": [],
        "Blue": [],
        "BS": [],
        "Error": [],
    },
    }

    with pdfplumber.open(path) as pdf:
        # Access pdf's page1 and extract its text
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        # Extract patient's name, DOB, and date of text  
        line1 = text.splitlines()[0]
        patient_data["Patient"] = line1[:line1.find(",")]
        patient_data["DOB"] = line1[line1.find(",")+2:]
        line2 = text.splitlines()[1]
        patient_data["Date"] = line2[line2.find("n")+2:line2.find("a")-1]+"-"+line2[line2.find("at")+3:line2.find("(")-1]

        # Crop original pdf to make extracting data easier, re-assign cropped page to var and extract text from cropped pdf
        first_page = first_page.crop((364, 0, first_page.width, first_page.height))
        text = first_page.extract_text()

        # Extracting Right Eye results from lines 3-27
        degree_axis = 0
        for line_index in range(3,27):
            linex = text.splitlines()[line_index]
            if degree_axis == 0 or degree_axis % 30 == 0:
                patient_data["RightEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
                patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 3)])
                patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 4)])
                patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 5)])
                if degree_axis == 0 or degree_axis % 45 == 0:
                    patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 5)+1:find_nth(linex, "°", 6)])
            else:
                if degree_axis % 45 == 0:
                    patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
            degree_axis += 15

        # Extracting Right Eye ave, error, and area
        # Average
        linex = text.splitlines()[27]
        patient_data["RightEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 1)])
        patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 2)])
        patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 3)])
        patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 4)])
        # Error
        linex = text.splitlines()[28]
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "%", 1)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "%", 2)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "%", 3)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "%", 4)])
        # Area
        linex = text.splitlines()[30]
        patient_data["RightEye"]["Form"].append(linex[:find_nth(linex, " ", 1)])
        patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, " ", 2)])
        patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, " ", 3)])
        patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, " ", 4)])
        patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 4)+1:])

        # Extracting Left Eye results from lines 34-27
        degree_axis = 0
        for line_index in range(34,58):
            linex = text.splitlines()[line_index]
            if degree_axis == 0 or degree_axis % 30 == 0:
                patient_data["LeftEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
                patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 3)])
                patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 4)])
                patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 5)])
                if degree_axis == 0 or degree_axis % 45 == 0:
                    patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 5)+1:find_nth(linex, "°", 6)])
            else:
                if degree_axis % 45 == 0:
                    patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
            degree_axis += 15 

        # Extracting Left Eye ave, error, and area
        # Average
        linex = text.splitlines()[58]
        patient_data["LeftEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 1)])
        patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 2)])
        patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 3)])
        patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 4)])
        # Error
        linex = text.splitlines()[59]
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "%", 1)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "%", 2)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "%", 3)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "%", 4)])
        # Area
        linex = text.splitlines()[61]
        patient_data["LeftEye"]["Form"].append(linex[:find_nth(linex, " ", 1)])
        patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, " ", 2)])
        patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, " ", 3)])
        patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, " ", 4)])
        patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 4)+1:])   

        return patient_data
    
def mod_data_extract(path):

    patient_data = {
    "Patient": None,
    "DOB": None,
    "Date": None,
    "RightEye": {
        "Form": [],
        "Red": [],
        "Green": [],
        "Blue": [],
        "BS": [],
        "Error": [],
    }, 
    "LeftEye": {
        "Form": [],
        "Red": [],
        "Green": [],
        "Blue": [],
        "BS": [],
        "Error": [],
    },
    }

    with pdfplumber.open(path) as pdf:
        # Access pdf's page1 and extract its text
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        # Extract patient's name, DOB, and date of text  
        line1 = text.splitlines()[0]
        patient_data["Patient"] = line1
        # patient_data["DOB"] = line1[line1.find(",")+2:]
        line2 = text.splitlines()[1]
        patient_data["Date"] = line2[line2.find("n")+2:line2.find("a")-1]+"-"+line2[line2.find("at")+3:line2.find("(")-1]

        # Crop original pdf to make extracting data easier, re-assign cropped page to var and extract text from cropped pdf
        first_page = first_page.crop((364, 0, first_page.width, first_page.height))
        text = first_page.extract_text()

        # Extracting Right Eye results from lines 3-27
        degree_axis = 0
        for line_index in range(3,27):
            linex = text.splitlines()[line_index]
            if degree_axis == 0 or degree_axis % 30 == 0:
                patient_data["RightEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
                patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 3)])
                patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 4)])
                patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 5)])
                if degree_axis == 0 or degree_axis % 45 == 0:
                    patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 5)+1:find_nth(linex, "°", 6)])
            else:
                if degree_axis % 45 == 0:
                    patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
            degree_axis += 15

        # Extracting Right Eye ave, error, and area
        # Average
        linex = text.splitlines()[27]
        patient_data["RightEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 1)])
        patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 2)])
        patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 3)])
        patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 4)])
        # Error
        linex = text.splitlines()[28]
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "%", 1)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "%", 2)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "%", 3)])
        patient_data["RightEye"]["Error"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "%", 4)])
        # Area
        linex = text.splitlines()[30]
        patient_data["RightEye"]["Form"].append(linex[:find_nth(linex, " ", 1)])
        patient_data["RightEye"]["Red"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, " ", 2)])
        patient_data["RightEye"]["Green"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, " ", 3)])
        patient_data["RightEye"]["Blue"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, " ", 4)])
        patient_data["RightEye"]["BS"].append(linex[find_nth(linex, " ", 4)+1:])

        # Extracting Left Eye results from lines 34-27
        degree_axis = 0
        for line_index in range(34,58):
            linex = text.splitlines()[line_index]
            if degree_axis == 0 or degree_axis % 30 == 0:
                patient_data["LeftEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
                patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 3)])
                patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 4)])
                patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 5)])
                if degree_axis == 0 or degree_axis % 45 == 0:
                    patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 5)+1:find_nth(linex, "°", 6)])
            else:
                if degree_axis % 45 == 0:
                    patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 2)])
            degree_axis += 15 

        # Extracting Left Eye ave, error, and area
        # Average
        linex = text.splitlines()[58]
        patient_data["LeftEye"]["Form"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "°", 1)])
        patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "°", 2)])
        patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "°", 3)])
        patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "°", 4)])
        # Error
        linex = text.splitlines()[59]
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, "%", 1)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, "%", 2)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, "%", 3)])
        patient_data["LeftEye"]["Error"].append(linex[find_nth(linex, " ", 4)+1:find_nth(linex, "%", 4)])
        # Area
        linex = text.splitlines()[61]
        patient_data["LeftEye"]["Form"].append(linex[:find_nth(linex, " ", 1)])
        patient_data["LeftEye"]["Red"].append(linex[find_nth(linex, " ", 1)+1:find_nth(linex, " ", 2)])
        patient_data["LeftEye"]["Green"].append(linex[find_nth(linex, " ", 2)+1:find_nth(linex, " ", 3)])
        patient_data["LeftEye"]["Blue"].append(linex[find_nth(linex, " ", 3)+1:find_nth(linex, " ", 4)])
        patient_data["LeftEye"]["BS"].append(linex[find_nth(linex, " ", 4)+1:])   

        return patient_data

# print(data_extract('pdfs/asayyed.pdf'))    
# print(len(data_extract('pdfs/fcftesterdata.pdf')["RightEye"]["Form"]))

# path = 'pdfs/asayyed.pdf'
# with pdfplumber.open(path) as pdf:
#     # Access pdf's page1 and extract its text
#     first_page = pdf.pages[0]
#     text = first_page.extract_text()
# print(text)


    

    



        
    