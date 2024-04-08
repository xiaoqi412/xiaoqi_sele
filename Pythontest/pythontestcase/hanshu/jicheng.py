# 继承

class Count():
    def add(self):
        return 1+1

class CountNew(Count):
    def acc(self):
        return 2-1

    def add(self):
        return 1 + 1

if __name__ == "__main__":
    a = CountNew()
    print(a.acc())
    a.add()

