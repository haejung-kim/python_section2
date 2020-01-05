# 성공 (블로그에서 파이썬 Blog 검색 (제목, Link, 입력시간) ->EXCEL파일 저장
#  file_name = 'result.xlsx'  --> xlsx.save(file_name) 파일이름 결정

import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from openpyxl import Workbook
xlsx = Workbook()
sheet = xlsx.active
sheet.append(['Title', 'link', 'Published date'])

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
        # print(pub_data_tag.text)
        sheet.append([title_tag.text,link, pub_data_tag.text])

except Exception as e:
    print(e)

finally:
    time.sleep(1)
    driver.quit()

file_name = 'd:/result.xlsx'
xlsx.save(file_name)

from my_email import send_mail
# send_mail('haejungkim', 'wowkk006@empas.com', '네이버 검색 결과입니다')
send_mail('haejungkim', 'wowkk006@empas.com', '네이버 검색 결과입니다', file_name)
