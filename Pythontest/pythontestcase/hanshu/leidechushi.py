class Count():
    def __init__(self,aa,bb):  #初始化  初始化里面的参数就是类里面实例化的参数，参数加了默认值，参数就是非必填参数了（实例化的时候就不用填了）
     # 当实例化的时候，首先会执行初始化的内容
     # print('hello world!')
     self.a = aa
     self.b = bb
     self.c = 'hello'  # 写死的，也可以传行参
     self.d = self.acc()
    def add(self):
        return self.a + self.b

    def acc(self):
        return self.a - self.b



    def hello(self):
        return self.c

if __name__ == '__main__':   # 类里面没有参数可以直接实例，类里面（初始化）有参数的话就不一样了
    a = Count(9,3)  # 类里面实例化的参数
    print(a.c)    # 访问属性不需要括号
    print(a.hello()) # 访问方法需要括号
    print(a.acc())
    print(a.d)   # 可以把方法变成属性
    # print(a.add())
    # print(a.acc())
    # print(a.c)





