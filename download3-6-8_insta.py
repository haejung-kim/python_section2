import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


driver = webdriver.Chrome('D:/python/chromedriver')

try:
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    elem = driver.find_element_by_link_text('로그인').click()

    time.sleep(3)
    elem = driver.find_element_by_name("username")
    elem.send_keys('wowkk006@empas.com')
    elem = driver.find_element_by_name("password")
    elem.send_keys('Ypp7521254!')
    elem.send_keys(Keys.RETURN)

    time.sleep(3)
    elem1 = driver.find_element_by_class_name("mt3GC")
    elem = elem1.find_element_by_xpath('./button[2]').click()
    time.sleep(3)

    #INPUT Tag 선택했을때
    # elem = driver.find_element_by_class_name("XTCLo")
    # elem.send_keys("#파이썬")
    # elem.send_keys(Keys.RETURN)

    #ACTION을 이용 (INPUT이 아닌, div TAG로 선택시
    elem = driver.find_element_by_class_name("eyXLr")
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.click()
    action.send_keys('#파이썬')
    action.perform()

    time.sleep(2)

    action.reset_actions()
    action.move_by_offset(0,2000)
    action.click()
    action.perform()
    input()

except Exception as e:
    print(e)

finally:
    time.sleep(10)
    driver.quit()
