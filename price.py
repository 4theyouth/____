import sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("helical-gist-437411-i3-e02672c49805.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("TOP80가격비교")
worksheet = spreadsheet.worksheet("결과")

batch_data = []

def add_columns_in_batch(data):
    global batch_data
    batch_data.append(data)
    
    if len(batch_data) >= 10:
        worksheet.insert_rows(batch_data)
        batch_data = []

import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

def quit_driver(driver):
    print("Timeout reached. Quitting driver.")
    driver.quit()

def get(href):
    driver = webdriver.Chrome()
    driver.get(href)

    timer = threading.Timer(20, quit_driver, [driver])
    timer.start()

    try:
        time.sleep(0.5)

        selector = driver.find_elements(By.CSS_SELECTOR, "a.bd_1fhc9")

        for i in selector: 
            print(i.text)
        selector[0].click()

        priceList = driver.find_elements(By.CSS_SELECTOR, "span._1LY7DqCnwR")
        price = priceList[len(priceList) - 1].text.replace(',', '')
        selector_list = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")

        for option in list(range(len(selector_list))):
            time.sleep(0.5)
            war = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")
            time.sleep(0.5)
            warName = war[option].text
            war[option].click()
            time.sleep(0.5)
            selector[1].click()
            ops = driver.find_elements(By.CSS_SELECTOR, "a.bd_3iRne")
            print(warName)
            time.sleep(0.5)
            for dti in ops:
                price_pattern = r"\(([\+\-\d,]+)원\)"
                match = re.search(price_pattern, dti.text)
                name = warName + "/" + dti.text.replace(price_pattern, "")
                try:
                    gamga = match.group(0).replace('(', '').replace(')', '').replace('원', '').replace(',', '')
                    print(int(gamga))
                    print(int(price))
                    add_columns_in_batch([href, name, int(gamga) + int(price)])
                except:
                    add_columns_in_batch([href, name, int(price)])
            time.sleep(0.5)
            selector[0].click()

    except Exception as e:
        print(f"An error occurred: {e}")
        if batch_data:
            print(4)
            sheet.add_column(batch_data)
            timer.cancel()
            driver.quit()
    finally:
        print(batch_data)
        print(2)
        if batch_data:
            print(3)
            sheet.add_column(batch_data)
            timer.cancel()
            driver.quit()

def finalize_batch():
    global batch_data
    if batch_data:
        worksheet.insert_rows(batch_data)
        batch_data = []