
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self,driver):
        # self.driver = webdriver.Firefox()
        self.driver = driver
    def find_element(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
        return element

    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)

    def click(self,locator):
        self.find_element(locator).click()

    def clear(self,locator):
        self.find_element(locator).clear()

    def is_exists(self,locator):
        # 判断元素存在
           try:
               self.is_located(locator)
               return True
           except:
               return False

    def is_alert_exsist(self):
        '''存在返回alert，不存在返回false'''
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            return True
        except:
            print('页面不存在alert,返回false')
            return False
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def text_is_in_element(self,locator, text):
        try:
            result = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def get_text(self,locator):
        return self.find_element(locator).text

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    mydriver = BasePage(driver)
    input_loc = ("id","kw")
    print(driver.title)
    mydriver.send_keys(input_loc,"yoyo") # 输入内容
    but_loc = ("id","su")
    mydriver.click(but_loc)
    re = mydriver.is_alert_exsist()
    locator = ("link text", "新闻")
    text = '新闻'
    f = mydriver.text_is_in_element(locator, text)
    print(f)


