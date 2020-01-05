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
driver.implicitly_wait(3)
driver.get('https://www.nate.com/')


driver.implicitly_wait(4)

driver.find_element_by_name('ID').send_keys('wowkk006@empas.com')
# time.sleep(1)
driver.implicitly_wait(3)
driver.find_element_by_name('PASSDM').send_keys('Ypp7521254!')
# time.sleep(1)
driver.implicitly_wait(3)


# XPATH를 통해 선택후 Click 누르기
driver.find_element_by_xpath('//*[@id="btnLOGIN"]').click()
# driver.find_element_by_xpath('//*[@id="btnLOGIN"]').submit()
