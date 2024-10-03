from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scroll_down(driver):
    # 페이지의 현재 높이
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 페이지 스크롤하기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 페이지 로딩 시간 대기
        time.sleep(2)  # 원하는 시간 동안 대기 (예: 2초)

        # 새로운 높이를 가져오기
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 새로운 높이가 이전 높이와 같으면 스크롤 종료
        if new_height == last_height:
            break
        last_height = new_height

# Selenium WebDriver 설정
def get(search_text):
    driver = webdriver.Chrome()  # 필요한 경우 executable_path를 설정하세요

    # 페이지 접속
    driver.get('https://search.shopping.naver.com/search/all?query=' + search_text + '&pagingSize=80')

    # 스크롤하여 모든 콘텐츠 로드하기
    naverpay = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul/li[3]/a')
    naverpay.click()
    time.sleep(0.3)
    scroll_down(driver)

    # time.sleep(2)

    # third_link = driver.find_element(By.CSS_SELECTOR, "div.paginator_inner__H_LDe > a:nth-of-type(3)")
    # third_link.click()
    # fourth_link = driver.find_element(By.XPATH, "//*[@id='__next']//div[contains(@class, 'paginator_list_paging__VxWMC')]//a[4]")
    # fourth_link.click()
    # second_button = driver.find_element(By.XPATH, "(//a[contains(@class, 'pagination_btn_page___ry_S') and contains(@class, '_nlog_click') and contains(@class, '_nlog_impression_element')])[2]")
    # second_button.click()

    # 특정 클래스명으로 모든 <a> 태그 찾기
    links = driver.find_elements(By.CSS_SELECTOR, "a.product_link__TrAac")

    # 각 링크의 href 속성 출력
    result = []
    for link in links:
        href = link.get_attribute('href')
        result.append(href)
    driver.quit()
    return result