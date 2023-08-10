from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

def find_empty():
    # returns index of the first empty row in spreadsheet 
    range_name = 'Sheet1!A1:BW1000'
    spreadsheet_id = '1H3SVc9dwfhemI0puZ8-n--FAtWykNH9nzygO2RstrDA'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    empty_row_index = len(rows)
    return empty_row_index
    
def write_range(range_name, values):
    spreadsheet_id = '1H3SVc9dwfhemI0puZ8-n--FAtWykNH9nzygO2RstrDA'  # get the ID of the existing sheet
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

