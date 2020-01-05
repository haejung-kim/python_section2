 # 이상하게 CLI가 안됨

import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('d:/python/chromedriver',options=chrome_options)

# chromedriver.exe로 표현안해도 됨
# driver = webdriver.Chrome('d:/python/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://google.com')

driver.save_screenshot("d:/pyton/Website111.png")

print(' 001성공')

driver.implicitly_wait(3)

driver.get('https://www.daum.net')
print(' 002성공')
driver.save_screenshot("d:/python/Website1122.png")
driver.quit()
print('스크린샷 완료')
