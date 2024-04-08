from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# class Login():
#     def __init__(self, a):
#         self.aa = a
#
#     def login(self, username, password):
#         self.aa.get('https://www.login.com')
#
#         self.aa.find_element(By.ID, "username").clear()
#         self.aa.find_element(By.ID, "username").send_keys(username)
#         self.aa.find_element(By.ID, "password").clear()
#         self.aa.find_element(By.ID, "password").send_keys(password)
#         self.aa.find_element(By.CLASS_NAME, "btn_login").click()
#
#     def logout(self):
#          self.aa.find_element(By.ID,"logout").click()

class Login():

    def __init__(self, tt):
        self.cc = tt

    def login(self, username, password):
        self.cc.get('https://account.chsi.com.cn/passport/login')
        self.cc.find_element(By.ID, "username").clear()
        self.cc.find_element(By.ID, "username").send_keys(username)
        self.cc.find_element(By.ID, "password").clear()
        self.cc.find_element(By.ID, "password").send_keys(password)
        self.cc.find_element(By.CLASS_NAME, "btn_login").click()

    def logout(self):
        self.cc.find_element(By.ID,"logout").click()

class Test(unittest.TestCase):

    # def setUp(self):
    #     self.a = Login(webdriver.Firefox)
    #     self.a.login(self, "aaa", "111")
    #
    # def tearDown(self):
    #     self.a.logout(self)

    # def test_001(self):

    def setUp(self):
        self.driver = webdriver.Firefox()
        bb = Login(self.driver)
        bb.login("aa", "111")

    def tearDown(self):
        bb = Login(self.driver)
        bb.logout()

    def test_001(self):
        self.driver = webdriver.Firefox()
        bb = Login(self.driver)
        bb.login("aa", "111")

        # 1...

        bb = Login(self.driver)
        bb.logout()


    def test_002(self):
        self.driver = webdriver.Firefox()
        bb = Login(self.driver)
        bb.login("aa", "111")

        # 2...

        bb = Login(self.driver)
        bb.logout()



