# class People():
#
#     def hand(self):
#         print('这是我对象的手')
#
#     def foot(self):
#         print('这是我对象的脚')
#
# if __name__ == '__main__':
#         a = People() # 先实例化，男朋友，类可以创建多个实例
#         a.hand()
#         a.foot()
#         b = People()   # 先实例化，女朋友
#         # del a # 对象销毁（了解就可以了）
#
# from selenium import webdriver
# driver1 = webdriver.Firefox()
# driver1.get('https://www.baidu.com')
#
# driver2 = webdriver.Chrome()
# driver2.get('https://www.baidu.com')
#
#
# class People():
#
#     def __init__(self):
#         self.girl = "girl"
#         self.live = "live"
#         print("start!")
#
#     def hand(self):
#         h = "这是我对象的手:%s and %s"%(self.girl, self.live)
#         return(h)
#     def foot(self):
#         f = "这是我对象的脚:%s and %s"%(self.girl, self.live)
#         return(f)
# if __name__ == "__main__":
#     # 创建一类的实例，初始化：girl/live
#     girlfriend = People()
#     # 访问类的属性
# print(girlfriend.girl)
# print(girlfriend.live)


class Test():
    def __init__(self):
        self.a = 5
        self.b = 4
        self.acc = self.add()
    def add(self):
        return self.a+self.b

a = Test()  # 实例化
print(a.add())  # 调用方法
print(a.acc )   # 调用属性
print(a.a)      # 调用属性

