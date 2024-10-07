import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import sheet 

batch_data = []

def quit_driver(driver):
    print("Timeout reached. Quitting driver.")
    driver.quit()

def add_columns_in_batch(data):
    global batch_data
    batch_data.append(data)


    if len(batch_data) >= 10:
        sheet.add_column(batch_data) 
        batch_data = [] 

def get(href):
    driver = webdriver.Chrome()
    driver.get(href)

    timer = threading.Timer(2000, quit_driver, [driver])
    timer.start()

    try:
        time.sleep(1)

        selector = driver.find_elements(By.CSS_SELECTOR, "a.bd_1fhc9")
        selector[0].click()

        priceList = driver.find_elements(By.CSS_SELECTOR, "span._1LY7DqCnwR")
        price = priceList[len(priceList) - 1].text.replace(',', '')
        selector_list = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")

        for option in list(range(len(selector_list))):
            time.sleep(0.5)
            war = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")
            time.sleep(0.5)
            warName = war[option].text
            print(f"FFFFFFF {warName}")
            war[option].click()
            time.sleep(0.5)
            selector[1].click()

            wrcplus_list = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")
            for wrcp in list(range(len(wrcplus_list))):
                print(f"wrcp: {wrcp}")
                time.sleep(1)
                wrcplus = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")
                wrcplusName = wrcplus[wrcp].text
                wrcplus[wrcp].click()
                time.sleep(1)
                selector[2].click()
                time.sleep(1)
                ops = driver.find_elements(By.CSS_SELECTOR, "a.bd_3iRne")
                print(warName)
                time.sleep(0.5)
                for dti in ops:
                    price_pattern = r"\(([\+\-\d,]+)원\)"
                    match = re.search(price_pattern, dti.text)
                    name = warName + "/" + wrcplusName + "/" + dti.text.replace(price_pattern, "")
                    try:
                        gamga = match.group(0).replace('(', '').replace(')', '').replace('원', '').replace(',', '')
                        print(int(gamga))
                        print(int(price))
                        add_columns_in_batch([href, name, int(gamga) + int(price)])
                    except:
                        add_columns_in_batch([href, name, int(price)])
                time.sleep(0.5)
                selector[1].click()
                time.sleep(0.5)

            selector[0].click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if batch_data:
            sheet.add_column(batch_data)
        timer.cancel()
        driver.quit()
