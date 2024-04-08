import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from hanshu import loginpage  #从文件夹导入模块
from hanshu.loginpage import login # 从文件夹模块导入函数，没有调用就是灰色
from hanshu import * #导入全部的

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://account.chsi.com.cn/passport/login")

    def login_seccuss(self):
        loginpage(self.driver,'admin',123456)
        # 判断结果
        new = self.driver.current_url
        # 断言
        self.assertEqual(new,'https://account.chsi.com.cn/account/account!show.action')

    def login_fail(self):
        loginpage(self.driver, 'admin', 45789)
        # 判断结果
        text = self.driver.find_element(By.ID, 'status').text
        # 断言
        self.assertEqual(text,'您输入的用户名或密码有误。')


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




