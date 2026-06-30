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
print(Calc.result)