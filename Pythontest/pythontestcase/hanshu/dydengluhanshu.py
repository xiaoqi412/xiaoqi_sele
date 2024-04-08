import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from hanshu import loginpage

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://account.chsi.com.cn/passport/login")

    def testlogin_seccuss(self):
        loginpage.login(self.driver,'18826507092','Ysynqimang412')
        # 判断结果
        new = self.driver.current_url
        # 断言
        self.assertEqual(new,'https://account.chsi.com.cn/account/account!show.action')

    def testlogin_fail(self):
        loginpage.login(self.driver, 'admin3', 45789)
        # 判断结果
        text = self.driver.find_element(By.ID, 'status').text
        # 断言
        self.assertEqual(text,'您输入的用户名或密码有误。')

    def loginout(self):
        loginpage.loginout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    # if下面都是自己测试的内容
    # driver = webdriver.Firefox()
    # driver.get("https://account.chsi.com.cn/passport/login")
    # time.sleep(1)
    # login(driver,'username',123456)
    unittest.main()




