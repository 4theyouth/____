import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google 스프레드시트에 접근하기 위한 인증
def get():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # 서비스 계정 JSON 파일 경로 설정
    creds = ServiceAccountCredentials.from_json_keyfile_name("aerial-tide-424006-u0-2e302c08c29b.json", scope)
    client = gspread.authorize(creds)

    # 스프레드시트 열기
    spreadsheet = client.open("TOP80가격비교")

    worksheet = spreadsheet.worksheet("검색어")  # 또는 worksheet = spreadsheet.worksheet("시트 이름")

    data = worksheet.get_all_records()

    result = [item['검색어'] for item in data]
    return result