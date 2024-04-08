
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www/baidu.com')

# 第一种方法
driver.find_element('id','kw').send_keys('yoyo')
driver.find_element('name','dfd').send_keys('yoyo')
driver.find_element('xpath','dfd').send_keys('yoyo')
driver.find_element('class name','dfd').send_keys('yoyo')
driver.find_element('tag name','dfd').send_keys('yoyo')
driver.find_element('partial link text','dfd').send_keys('yoyo')
driver.find_element('link text','dfd').send_keys('yoyo')
driver.find_element('css selector','dfd').send_keys('yoyo')
# 第二种方法
driver.find_element(By.ID,'KW').send_keys('youyo')
driver.find_element(By.NAME,'KW').send_keys('youyo')
driver.find_element(By.XPATH,'KW').send_keys('youyo')
driver.find_element(By.CLASS_NAME,'KW').send_keys('youyo')
driver.find_element(By.TAG_NAME,'KW').send_keys('youyo')
driver.find_element(By.LINK_TEXT,'KW').send_keys('youyo')
driver.find_element(By.PARTIAL_LINK_TEXT,'KW').send_keys('youyo')
driver.find_element(By.CSS_SELECTOR,'KW').send_keys('youyo')

