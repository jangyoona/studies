# python은 반환값이 여러개일 때 자동으로 튜플을 만들어 반환한다.

def calc(check, *value):
    num=0
    for i in value:
        num = num + i
    
    if check:
        return num, set(value), check
    else:
        return set(value)
    
k = calc(1, 1, 2, 3, 4, 1, 2)
print(k)
# 결과
# (13, {1, 2, 3, 4}, 1)

# 튜플이 아닌, 각 value 추출 원할 경우 언패킹
a, b, c = calc(1, 1, 2, 3, 4, 1, 2)
print(a)
print(b)
print(c)
# 결과
# 13
# {1, 2, 3, 4}
# 1