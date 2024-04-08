


def hanshu(a):
    return a+1
print(hanshu(1)) # 函数对象
a = hanshu(6)
print(a)
b = lambda x: x+1 # 匿名函数
print(b(6))
def add(a,b):
    return a+b
c = lambda x,y:x+y
print(c(4,6))

if __name__ == '__main__':

    print(a)
    print(b(6))
