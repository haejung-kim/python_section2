# 성공 (블로그에서 파이썬 Blog 검색 (제목, Link, 입력시간)

import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
driver = webdriver.Chrome('D:/python/chromedriver')

try:
    driver.get('https://www.naver.com/')
    elem = driver.find_element_by_id('query')
    elem.send_keys("파이썬")
    elem.send_keys(Keys.RETURN)
    div = driver.find_element_by_class_name('_blogBase')
    blogs=div.find_elements_by_xpath('./ul/li')
    # print(blogs[0].text)

    for blog in blogs:
        title_tag = blog.find_element_by_class_name('sh_blog_title')
        # print(title_tag.text)
        link = title_tag.get_attribute('href')
        # print(link)
        pub_data_tag = blog.find_element_by_class_name('txt_inline')
        print(pub_data_tag.text)

except Exception as e:
    print(e)
finally:
    time.sleep(1)
    driver.quit()
