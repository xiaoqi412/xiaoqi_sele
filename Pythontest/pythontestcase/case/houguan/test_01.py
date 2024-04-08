import unittest
from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

class Test2(unittest.TestCase):

    def test001(self):
        u'''登录成功的案例'''
        time.sleep(1)
        print('ssssssss')


    def test002(self):
        u'''登录失败的案例'''
        time.sleep(1)
        print('fgfghfghghg')

    def test003(self):
        u'''登录不ok的案例'''
        time.sleep(1)
        print('dffgf')
        a = 1
        b = 1
        self.assertEqual(a,b)



if __name__ == "__main__":
    unittest.main()