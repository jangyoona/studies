t=[1, 2, '1', '2', '3', '4']
t[2:] = 'abc'
print(t)

# 단일 대입
t[0] = [1, 2]
print('단일 대입 결과: {}'.format(t))

# 슬라이스 대입
# 슬라이스는 반드시 iterable을 기대함.
# 따라서, 위 단일 대입과 index 범위는 같아 보일 수 있으나
# 대입되는 iterable 요소를 펼처서 값을 넣는다.
t[1:2] = [5, 6]
print('slice 대입 결과: {}'.format(t))

# print(t.index(6))