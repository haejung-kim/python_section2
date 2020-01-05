import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#driver = webdriver.Chrome('d:/python/chromedriver.exe')
driver = webdriver.PhantomJS('D:/Python/phantomjs')

driver.implicitly_wait(3)
# 무조건 5초가 아님, 그전에 Loading 되면 빨리 동작함

driver.get('https://google.com')
driver.save_screenshot('d:/python/website11.png')
# 처음에 C driver에 저장했는데 안됨 ,why? 관리자 권한으로 실행안해서

driver.implicitly_wait(3)
driver.get('https://www.daum.net')
driver.save_screenshot('d:/python/website12.png')

driver.quit()
print('스크린샷 완료')
