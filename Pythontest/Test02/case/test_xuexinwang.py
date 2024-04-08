import unittest
from page.xuexinwangpage import login_url,XueXinWangPage
from selenium import webdriver

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()   # 只打开一次浏览器
        cls.logindriver = XueXinWangPage(cls.driver)


    def setUp(self):
        self.driver.get(login_url)  # 每次登录都走登录页

    def test_login_01(self):
        """登录成功的"""
        # 输入账号
        self.logindriver.input_username("18826507092")
        # 输入密码
        self.logindriver.input_password("Ysynqimang412")
        # 点击登录按钮
        self.logindriver.click_button()
        # 获取登录结果，判断text是否在元素里面
        result = self.logindriver.get_login_text()
        print(result)
        # 期望结果
        exp = "消息推送"
        # 断言
        self.assertEqual(result,exp)

    def test_login_02(self):
        """登录失败的"""
        # 输入账号
        self.logindriver.input_username("18826507092")
        # 输入密码
        self.logindriver.input_password("Ysynqimang413")
        # 点击登录按钮
        self.logindriver.click_button()
        # 获取登录结果，判断text是否在元素里面
        result = self.logindriver.get_login_text()
        print(result)
        # 期望结果
        exp = "您输入的用户名或密码有误。"
        # 断言
        self.assertEqual(result,exp)

    def tearDown(self):
        self.driver.delete_all_cookies()  # 清空所有的cookies

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
