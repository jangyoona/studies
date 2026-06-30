# python에서 java나 c++처럼 강제되는 private 접근 제어자가 없다.
# 따라서, 간단히 클래스 변수에 접근이 가능하다.

class Calc:
    result = 0
    def setdata(self, fir, sec):
        self.fir = fir
        self.sec = sec

    def add(self):
        Calc.result += 1 # 클래스 변수 값 수정
        self.result = self.fir + self.sec

    def getdata(self):
        print(self.result, end= ' ')
        print(Calc.result)

a = Calc()
b = Calc()
a.setdata(5, 10)
b.setdata(3, 2)

a.add()
a.getdata()

b.add()
b.getdata()

Calc.result += 1
print(f'Calc.result={Calc.result}')
#Calc.result = 3

# t) 인스턴스에서 속성을 찾을 때 존재하지 않을 경우
#    상위로 올라가 클래스 변수를 찾아 반환한다.
print(f'a.result 삭제 전 result={a.result}')
print(f'b.result 삭제 전 result={b.result}')
del(a.result)
del(b.result)
print(f'a.result 삭제 후 result={a.result}')
print(f'b.result 삭제 후 result={b.result}')