# //encar 자동 매물 조회  (현대 - i30 , 2011~2015년 선택후 검색 누르기 )
import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('D:/python/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(1)
driver.get('http://www.encar.com/index.do')

time.sleep(1)
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="manufact"]/a/span[1]').click()

driver.find_element_by_xpath('//*[@id="manufactListText"]/ul[1]/li[1]/a').click()

driver.find_element_by_xpath('//*[@id="seriesItemList"]/li[10]/a').click()
driver.find_element_by_xpath('//*[@id="mdlItemList"]/li[4]/a').click()

driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a').click()


special=driver.find_element_by_class_name('special')
li_specials=special.find_elements_by_xpath('./div/ul/li')

for li in li_specials:
        brand = li.find_element_by_xpath('./a/span[2]/span/em')
        print(brand.text)
        year = li.find_element_by_xpath('./a/span[4]/span')
        print(year.text)
        KM = li.find_element_by_xpath('./a/span[3]/span[2]')
        print(KM.text)
        type = li.find_element_by_xpath('./a/span[3]/span[3]')
        print(type.text)
        location = li.find_element_by_xpath('./a/span[3]/span[4]')
        print(location.text)
        price = li.find_element_by_xpath('./a/span[4]/span/strong')
        print(price.text)

time.sleep(3)




# XPATH를 통해 선택후 Click 누르기
