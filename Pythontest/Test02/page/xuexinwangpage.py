from selenium import webdriver
from common.base import BasePage


login_url = "https://account.chsi.com.cn/passport/login"

class XueXinWangPage(BasePage):
    usernameloc = ("id","username")
    passwordloc = ("id","password")
    buttonloc = ("class name","btn_login")
    succloc = ("link text","消息推送")

    def input_username(self,text):
        self.send_keys(self.usernameloc,text)

    def input_password(self,text):
        self.send_keys(self.passwordloc,text)

    def click_button(self):
        self.click(self.buttonloc)

    def get_login_text(self):
        try:
            t = self.get_text(self.succloc)
            return t
        except:
            print("元素获取异常，返回'' ")
            return ''


if __name__ == "__main__":
    driver = webdriver.Firefox()
    xuexiewang = XueXinWangPage(driver)





