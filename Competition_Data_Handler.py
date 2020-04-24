from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of the spreadsheet to be read from.
SPREADSHEET_ID = '1SWTRqL6k01RxmQKH-kC982g1cRjQCZB9h0jntFswlcs'
RANGE_NAME = 'Sheet1!A2:H2'

# Writes data to Google spreadsheet at cell address
def writeCell(sheet, cellAdr, cellValue):
    cellBody = {'values': [[cellValue], []]}
    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                   range=cellAdr,
                                   valueInputOption='RAW',
                                   body=cellBody).execute()

def main():
    tokenPath = '/hom/pi/bridgebreaker/Competition Data Handler'
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(tokenPath + 'token.pickle'):
        with open(tokenPath + 'token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, lets the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                tokenPath + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Saves the credentials for the next run.
        with open(tokenPath + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Spreadsheet Data')
        for row in values:
            # Print spreadsheet data.
            print('%s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4]))
    # Write spreadsheet data.
    power = 100
    writeCell(sheet=sheet, cellAdr='Sheet1!F2', cellValue=power)

if __name__ == '__main__':
    main()