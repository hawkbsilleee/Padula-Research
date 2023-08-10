from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

def find():
    # returns index of the first empty row in spreadsheet 
    range_name = 'Sheet1!A1:BW1000'
    spreadsheet_id = '1H3SVc9dwfhemI0puZ8-n--FAtWykNH9nzygO2RstrDA'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])

print(find())
