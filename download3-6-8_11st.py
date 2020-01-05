# 11번가 판매자, 이름 ,상품가격 -> EXCEL
import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from openpyxl import Workbook
xlsx = Workbook()
sheet = xlsx.active
sheet.append(['seller', 'product', 'price'])

driver = webdriver.Chrome('D:/python/chromedriver')

try:
    driver.get('https://www.11st.co.kr/')
    elem = driver.find_element_by_id('AKCKwd')
    elem.send_keys("자전거")
    elem.send_keys(Keys.RETURN)

    # elems = driver.find_elements_by_xpath('//*[@id="product_listing"]/div[6]/div/ul/li')
    elems = driver.find_elements_by_xpath("//li[contains(@id,'thisClick_')]")

    for elem in elems:
        seller_tag = elem.find_element_by_xpath('./div/div[4]/p[1]/a')
        # seller_tag = elem.find_element_by_class_name('info_tit')
        # print(seller_tag.text)
        product_tag = elem.find_element_by_xpath('./div/div[2]/p/a')
        # product_tag = elem.find_element_by_class_name('benefit_tit')
        # print(product_tag.text)
        price_tag = elem.find_element_by_xpath('./div/div[3]/div[1]/span/strong')
        # price_tag = elem.find_element_by_class_name('sale_price')
        # print(price_tag.text)
        sheet.append([seller_tag.text,product_tag.text,price_tag.text])

except Exception as e:
    print(e)

finally:
    time.sleep(1)
    driver.quit()

file_name = 'd:/result_11st.xlsx'
xlsx.save(file_name)

from my_email import send_mail
send_mail('haejungkim', 'wowkk006@empas.com', '11번가 검색 결과입니다', file_name)
