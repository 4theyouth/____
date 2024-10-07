import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("helical-gist-437411-i3-e02672c49805.json", scope) # CHANGE ME
client = gspread.authorize(creds)

spreadsheet = client.open("TOP80가격비교") # CHANGE ME
worksheet = spreadsheet.worksheet("결과") # CHANGE ME
def add_column(column):
    worksheet.append_row(column)
