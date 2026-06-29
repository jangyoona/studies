# python 클래스

class Car():
    '''자동차'''

taxi = Car()
taxi.name = '택시'

print(taxi.name)



class Car2():
    '''자동차'''

    def run(self):
        print('{}가 달립니다.'.format(self.name))

taxi2 = Car2()
taxi2.name = '택시'
taxi2.run()