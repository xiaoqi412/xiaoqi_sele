

class Count():

    def a1(self,a,b):   # 类里面的叫方法
        return a+b

    def a2(self,a,b):
        return a-b

    def a3(self,a,b):
        return a*b

    def a4(self,a,b):
        return a/b

    def ann(self,a,b):
        return self.a1(a,b)*self.a2(a,b) #self是类本身的实例参数



if __name__ == '__main__':
    # Count().a1(3,6)
    # print(Count().a1(3,6))     # 上面两行等价于下面三行
    m = Count()
    m.a1(9,3)
    print(m.a1(9,3))

    # q = Count()
    # p =q.ann(2,1)
    # print(q.ann(2,1))
    print(m.ann(3,1))


ae = [' 1', '22', '44']
print(ae)

# p = ['2', '33', '45a']
# print(type(p))
# print(p[2])

mr = ['2', '33', '46a']
print(type(mr))
print(mr[1])

