
from selenium.webdriver.common.by import By

def login(driver,username,password):
    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").clear()
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CLASS_NAME,"btn_login").click()

def login2(driver,username,password):
    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").clear()
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CLASS_NAME,"btn_login").click()

def loginout():
    print('退出函数')


# print(88888)

def say():
    print(222222)

say()



if __name__ == '__main__':
    print(44444)
    print(__name__)



print(111111111111)
print(__name__)

class Tfdf:
    def login123(self):
        print(3333)

a = Tfdf()   # 调用类的时候先返回实例
a.login123()
Tfdf().login123()# 等价于上面两行


if __name__ == '__main__':
    print(99999)

    print(1234)

