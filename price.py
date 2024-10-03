from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import sheet

def get(href):
    driver = webdriver.Chrome()
    driver.get(href)

    time.sleep(0.5)

    selector = driver.find_elements(By.CSS_SELECTOR, "a.bd_1fhc9")

    for i in selector: print(i.text)
    selector[0].click()

    priceList = driver.find_elements(By.CSS_SELECTOR, "span._1LY7DqCnwR")
    price = priceList[len(priceList) - 1].text.replace(',', '')
    selector_list = driver.find_elements(By.CSS_SELECTOR, "li.bd_1y1pd")
    print(selector_list)
    print(price)
    
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
                sheet.add_column([href, name, int(gamga) + int(price)])
            except:
                sheet.add_column([href, name, int(price)])
        time.sleep(0.5)
        selector[0].click()
    time.sleep(0.5)
    driver.quit()