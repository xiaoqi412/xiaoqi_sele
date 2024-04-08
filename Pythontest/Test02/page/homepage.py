from common.base import BasePage
from selenium import webdriver
home_url = "http://www.cnblogs.com/youyouketang/"

class HomePage(BasePage):

    bky_loc = ("id","blog_nav_sitehome")
    nav_loc = ("id", "blog_nav_myhome")
    xsb_loc = ("id", "blog_nav_newpost")

    def click_bky(self):
        self.click(self.bky_loc)

    def click_nav(self):
        self.click(self.nav_loc)

    def click_xsb(self):
        self.click(self.xsb_loc)

    def is_exsist_img(self):
        img_loc = ("xpath",".//*[@id='logo']/h1/a/img")
        return self.is_exsist(img_loc)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(home_url)
    homedriver = HomePage(driver)
    homedriver.click_bky()

