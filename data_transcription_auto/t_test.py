import pandas as pd 
from auth import spreadsheet_service
from auth import drive_service
import pandas as pd 
from scipy.stats import ttest_ind

def get_data():
    # returns index of the first empty row in spreadsheet 
    range_name = 'Sheet1!A26:BX1000'
    spreadsheet_id = '1H3SVc9dwfhemI0puZ8-n--FAtWykNH9nzygO2RstrDA'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    return rows

# print(get_data()[-1][59])
# pd.DataFrame(data=dataset_dict)
def extract(index): 
    dataset = get_data()
    dataset_dict = {'Control': [], 'Experimental': []}
    for patient in dataset:
        if patient[-1] == 'Control': 
            dataset_dict['Control'].append(patient[index])
        if patient[-1] == 'Experimental': 
            dataset_dict['Experimental'].append(patient[index])
    dataset_df = pd.DataFrame({ key:pd.Series(value) for key, value in dataset_dict.items() })
    return dataset_df

df = extract(59)
ttest_ind(df['Control'], df['Experimental'])





