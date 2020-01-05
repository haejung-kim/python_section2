import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('d:/python/chromedriver',options=chrome_options)
# driver = webdriver.Chrome('d:/python/chromedriver')

# driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)    # chrome Loading 위해

driver.get('https://nid.naver.com/nidlogin.login?')

driver.find_element_by_name('id').send_keys('wowkk006')
driver.implicitly_wait(1)
driver.find_element_by_name('pw').send_keys('1q2w3e4r')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()



print('스크린샷 완료')
