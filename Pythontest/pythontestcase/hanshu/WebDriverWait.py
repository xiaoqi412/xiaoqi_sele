from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 这种可以
from selenium.webdriver.support.wait import WebDriverWait # 这种也可以
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

sou_loc = ("id","kw")
WebDriverWait(driver,10).until(lambda x: x.find_element(*sou_loc))
but_loc = ("id","su")



# element = driver.find_element(By.ID,"kw").click()  # element是查找元素的对象

# element = WebDriverWait(driver,10).until(lambda x: x.find_element(By.ID,"kw11"))
# print(element)



'''
from selenium.webdriver.support.wait import WebDriverWait \n
# 在timeout时间内直到元素出现
element = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "someId")) \n
# 在timeout时间内直到元素消失
is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\\ \n
until_not(lambda x: x.find_element(By.ID, "someId").is_displayed())
'''


class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,locator):
        element = WebDriverWait(driver,10).until(lambda x: x.find_element(*locator))
        return element

    # def send_keys(self,locator,text):
    #     self.find_element().send_keys(text)
    #
    # def click(self,locator):
    #     self.find_element(locator).click()
    #
    # if __name__ == "__main__":
    #     driver = webdriver.Firefox()
    #     mydriver = Base(driver)
    #     driver.get('https://www.baidu.com')
    #     inp_loc = ("id","kw")
    #     mydriver.send_keys(inp_loc,"yoyo") # 输入内容
    #     but_loc = ("id","kw")
    #     mydriver.click(but_loc)