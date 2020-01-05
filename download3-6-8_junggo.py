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
    driver.get('https://cafe.naver.com/joonggonara')
    elem = driver.find_element_by_id('topLayerQueryInput')
    elem.send_keys("자전거")
    elem.send_keys(Keys.RETURN)

    # 모든 iframe 확인
    # iframes = driver.find_elements_by_css_selector('iframe')
    # for iframe in iframes:
        # print(iframe.get_attribute('name'))
    time.sleep(1)
    iframe = driver.find_element_by_id('cafe_main')
    driver.switch_to_frame(iframe)
    elem = driver.find_element_by_id('content-area')
    elem1 = elem.find_element_by_xpath('./div[1]/div[5]/table')
    blogs = elem1.find_elements_by_xpath('./tbody/tr')
    for blog in blogs:
        title_tag = blog.find_element_by_xpath('./td[1]/div[2]/div/a')
        print(title_tag.text)

except Exception as e:
    print(e)

finally:
    time.sleep(3)
    driver.quit()
