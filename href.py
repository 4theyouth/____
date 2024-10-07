from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get(search_text):
    driver = webdriver.Chrome()
    driver.get('https://search.shopping.naver.com/search/all?query=' + search_text + '&pagingSize=80')
    naverpay = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul/li[3]/a')
    naverpay.click()
    time.sleep(0.3)
    scroll_down(driver)
    links = driver.find_elements(By.CSS_SELECTOR, "a.product_link__TrAac")
    result = []
    for link in links:
        href = link.get_attribute('href')
        result.append(href)
    print(len(result))
    driver.quit()
    return result