from selenium import webdriver
from selenium.webdriver.common.by import By

class AA():

    a = 10
    b = 'fffn'

    def logout123(self):
        print(111)

class Login():
    def __init__(self, driver):
        self.a = driver

    def login(self,url,username,password):
        self.a.get(url)
        self.a.find_element(By.ID, "username").clear()
        self.a.find_element(By.ID, "username").send_keys(username)
        self.a.find_element(By.ID, "password").clear()
        self.a.find_element(By.ID, "password").send_keys(password)
        self.a.find_element(By.CLASS_NAME, "btn_login").click()

    def logout(self):
       self.a.find_element(By.ID,"FHFHFH").click()


import unittest
class Test(unittest.TestCase):


    def test_001(self):
        driver = webdriver.Firefox()
        b = Login(driver)
        b.login('','18826507092','ysynqimang412')
        b.logout()

    def test_002(self):
        driver = webdriver.Chrome()
        b = Login(driver)
        b.login('', '18826507092', 'ysynqimang412')
        b.logout()

