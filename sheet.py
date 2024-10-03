import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google 스프레드시트에 접근하기 위한 인증
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# 서비스 계정 JSON 파일 경로 설정
creds = ServiceAccountCredentials.from_json_keyfile_name("aerial-tide-424006-u0-2e302c08c29b.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("TOP80가격비교")
# 워크시트 선택 (예: 첫 번째 시트)
worksheet = spreadsheet.worksheet("결과")
# 스프레드시트 열기
def add_column(column):
    worksheet.append_row(column)
