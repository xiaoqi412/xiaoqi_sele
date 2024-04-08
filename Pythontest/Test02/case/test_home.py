from selenium import webdriver
from page.loginpage import LoginPage,login_url
from page.homepage import HomePage,home_url
import unittest

class HomeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.homedriver = HomePage(self.driver)
        # 先登录
        self.driver.get(login_url)
        self.logindriver.login()

    def test_click_bky(self):
        self.driver.get(home_url) # 打开首页
        self.homedriver.click_bky() # 点首页的bky按钮
        # 判断结果
        result = self.homedriver.is_exsist_img()
        print()
        # 断言
        self.assertTrue(result)




