# 성공 네이버 뉴스 TOP 10

import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
driver = webdriver.Chrome('D:/python/chromedriver')

try:
    driver.get('https://news.naver.com/')
    elem1 = driver.find_element_by_id('right.ranking_contents')
    print('11')
    childs = elem1.find_elements_by_tag_name('li')
    print('12')

    for child in childs:
        print(child.text)

except Exception as e:
    print(e)
finally:
    time.sleep(3)
    driver.quit()
