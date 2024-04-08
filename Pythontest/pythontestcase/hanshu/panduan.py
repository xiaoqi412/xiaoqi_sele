from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www/baidu.com')

inp_loc = ("id","kw")
element = WebDriverWait(driver,10).until(EC.presence_of_element_located(inp_loc))
element.send_keys("yyyy")


class Base():

    def __init__(self,driver):
        # self.driver = webdriver.Firefox()
        self.driver = driver
    def is_alert_exsist(self):
        '''存在返回alert，不存在返回false'''
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            return True
        except:
            print('页面不存在alert,返回false')
            return False


    def text_is_in_element(self, locator):
        try:
            result = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator))
            return result
        except:
            return False







if __name__ == "__main__":
        driver = webdriver.Firefox()
        mydriver = Base(driver)
        driver.get('https://www.baidu.com')
        re = mydriver.is_alert_exsist()

