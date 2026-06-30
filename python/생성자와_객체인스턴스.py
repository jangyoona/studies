class Test:
    def __init__(self, x, y):
        print('생성자 호출')
        self.x = x
        self.y = y
    
    def calc(self):
        result = self.x * self.y
        return result
    
    def __del__(self):
        print('소멸자 호출')
    
    def __str__(self):
        return'toString 이요. x={}, y={}'.format(self.x, self.y)
    
    def __eq__(self, other):
        print('equals() override와 유사. a == b 실행 시 호출됨')
        return self.x == other.x

# __init__ 호출
a = Test(5, 2)
print(a.calc())

# __del__ 호출
del(a)

# __str__ 호출
b = Test(1, 2)
print(str(b))

# __eq__ 호출
print(b == Test(2,3))