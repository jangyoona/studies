# print 출력 형식 관련

a = 'python'
b = 'github'

# 치환
format1 = '{}'.format(a)
format2 = '{} {}'.format('python', a)
format3 = '{}점'.format(100)
format4 = f'a는 {a}입니다.'
format5 = f'{a + b}'

print(format1)
print(format2)
print(format3)
print(format4)
print(format5)

# 정렬
print(f'{a:<10}') # 왼쪽
print(f'{a:>10}') # 오른쪽
print(f'{a:^10}') # 가운데