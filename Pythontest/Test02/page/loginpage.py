from common.base import BasePage
from selenium import webdriver

login_url = "https://passport.cnblogs.com/user/signin"

class LoginPage(BasePage):
    username_loc = ("id","mat-input-0")
    psw_loc = ("id","mat-input-1")
    but_loc = ("class name","mat-button-wrapper")
    remember_loc = ("class name","mat-checkbox-label")
    def input_username(self,text):
        self.send_keys(self.username_loc,text)

    def input_pws(self, psw):
        self.send_keys(self.psw_loc, psw)

    def click_login_button(self):
        self.click(self.but_loc)

    def click_remember_button(self):
        self.click(self.remember_loc)

    def login(self,user="admin",psw="111111"):
        '''登录流程'''
        self.input_username(user)
        self.input_pws(psw)
        self.click_login_button()

    def is_login_success(self):
        success_loc = ("","")
        result = self.text_is_in_element(success_loc,"上海-悠悠")
        return result

if __name__== '__main__':
    driver = webdriver.Firefox()
    login_driver = LoginPage(driver)
    driver.get(login_url)
    login_driver.login()






