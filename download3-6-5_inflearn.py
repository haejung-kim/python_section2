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
driver.get('https://www.inflearn.com/')

driver.implicitly_wait(1)

# 오른쪽 상단 누름  (copy xPath사용)
driver.find_element_by_xpath('//*[@id="signin"]').click()
# ID  (copy xPath사용)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/label[1]/input').send_keys('wowkk006@empas.com')
# PW  (copy xPath사용)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/label[2]/input').send_keys('Ypp7521254!')
# Click  (copy xPath사용)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/button').click()

test = driver.find_element_by_class_name('section.section.courses.my_recent_courses')
test1 =test.find_element_by_xpath('./div/div/h1')

print (test1.text)
print (driver.title)
time.sleep(1)
