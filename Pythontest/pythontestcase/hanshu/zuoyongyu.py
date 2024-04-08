a = 1 # 全局变量，传在当前脚本的任意位置

class Count():

    b = 10 # clsss里面的全局变量,参数b的作用域在class范围里面有效，出了这个class范围，就失效了
    def __init__(self):
        e = 40  # e的作用域只在init里面有效，因为没有加self
        self.d = 30 #d跟b的作用域差不多的


    def add(self):
        c = 20 # c的作用域只在当前定义的方法里面
        print(c)
        return a + 1
        return b
        print(self.b)
        print(self.d)

    print(a+100)


    def acc(self):
        return self.b-5
        print(self.b)


if __name__ == '__main__':
    q = Count()
    # print(q.add())
    # print(a+10)
    # print(q.acc())
    print(q.b)
    print(q.d)

