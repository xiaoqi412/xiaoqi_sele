import unittest

import ddt

from page.xuexinwangpage import login_url,XueXinWangPage
from selenium import webdriver

# test_date1 = {"uaername":"18826507092","password":"Ysynqimang412","exp":"消息推送",}
# test_date2 = {"uaername":"18826507092","password":"Ysynqimang413","exp":"您输入的用户名或密码有误.",}

data = [{"uaername":"18826507092","password":"Ysynqimang412","exp":"消息推送",},
        {"uaername":"18826507092","password":"Ysynqimang413","exp":"您输入的用户名或密码有误。",}
        ]
@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()   # 只打开一次浏览器
        cls.logindriver = XueXinWangPage(cls.driver)


    def setUp(self):
        self.driver.get(login_url)  # 每次登录都走登录页

    def logintest(self,uaername,password,exp):
        # 输入账号
        self.logindriver.input_username(uaername)
        # 输入密码
        self.logindriver.input_password(password)
        # 点击登录按钮
        self.logindriver.click_button()
        # 获取登录结果，判断text是否在元素里面
        result = self.logindriver.get_login_text()
        print(result)
        # 返回布尔值
        return result == exp

    @ddt.data(*data)
    def test_login_01(self,testdata):
        print(testdata)
        """登录成功的案例"""
        result = self.logintest(**testdata)
        self.assertTrue(result)

    @ddt.data(*data)
    def test_login_02(self,testdata):
        print(testdata)
        """登录失败的案例"""
        result = self.logintest(**testdata)
        self.assertTrue(result)

    def tearDown(self):
        self.driver.delete_all_cookies()  # 清空所有的cookies

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
