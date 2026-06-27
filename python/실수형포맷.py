# print 출력 형식 관련

value = 3.141592
value = 3.199

format1 = f'{value:.2f}'    # 소수 둘째 자리까지 표시, str 반환
format2 = '%.2f' % value    # 소수 둘째 자리까지 표시, str 반환 old
format3 = round(value, 2)   # 소수 둘째 자리로 반올림, float 반환(끝의 0은 표시되지 않을 수 있음)

print(format1)
print(format2)
print(format3)
