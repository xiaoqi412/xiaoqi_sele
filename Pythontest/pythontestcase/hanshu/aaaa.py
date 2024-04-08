# from hanshu import loginpage
#
# loginpage.say()
#
# print(__name__)
#
# if __name__ == '__main__':
#     print(5555)



class People():

    def __init__(self):
        self.girl = "girl"
        self.live = "live"
        print("start!")

    def hand(self):
        h = "这是我对象的手:%s and %s"%(self.girl, self.live)
        return(h)
    def foot(self):
        f = "这是我对象的脚:%s and %s"%(self.girl, self.live)
        return(f)
if __name__ == "__main__":
    # 创建一类的实例，初始化：girl/live
    girlfriend = People()
    # 访问类的属性
print(girlfriend.girl)
print(girlfriend.live)
