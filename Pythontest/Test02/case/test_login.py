import unittest
from selenium import webdriver
from page.loginpage import LoginPage,login_url

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.driver.get(login_url)

    def test_login(self):
        # 输入账号
        self.logindriver.input_username("admin")
        # 输入密码
        self.logindriver.input_pws("22222")
        # 点击登录按钮
        self.logindriver.click_login_button()
        # 获取登录结果，判断text是否在元素里面
        result = self.logindriver.is_login_success()
        # 断言
        self.assertTrue( result)
