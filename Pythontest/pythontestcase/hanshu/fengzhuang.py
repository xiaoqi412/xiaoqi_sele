
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# 函数
def login(driver, username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn_login").click()
class Login():

    def __init__(self, driver):
         self.driver = driver
    def login(self, username, password):
         self.driver.find_element(By.ID, "username").clear()
         self.driver.find_element(By.ID, "username").send_keys(username)
         self.driver.find_element(By.ID, "password").clear()
         self.driver.find_element(By.ID, "password").send_keys(password)
         self.driver.find_element(By.CLASS_NAME, "btn_login").click()

    def logout(self):
         self.driver.find_element(By.ID,"logout").click()


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.login.com')
        self.logindriver = Login(self.driver)   # 每个用例都要调用到登录,先实例
        self.logindriver.login('18826507092', 'ysynqimang412')  # 通过实例调用方法

    def test_001(self):
        # 调用登录，先实例化,需要传参数driver
        # 登录完之后，操作页面上的元素
        self.driver.find_element(By.ID,'dgffgfg').click()
        # 退出登录
        self.logindriver.logout()

    def test_002(self):
        # 调用登录，先实例化,需要传参数driver
        # 登录完之后，操作页面上的元素
        self.driver.find_element(By.ID, 'dgffgfg').click()
        # 退出登录
        self.logindriver.logout()




