# list에서 값을 이용하여 위치를 찾기
# index()
def safe_index(list, value):
    if value in list :
            return list.index(value)
    else :
        return None


print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))

# ========================================================================================

# list 유틸 함수
list = [1, 2, 3, 4]

# 길이
print('list 길이는: {}'.format(len(list)))

# list 최소값/최대값/총합
min(list)
max(list)
sum(list)

# 개수 반환
numbers = [1, 2, 3, 4, 1, 1]
print('총 1의 개수는: {}'.format(numbers.count(1)))

# 기본 추가
list.append(5)
print('맨 뒤에 값 추가: {}'.format(list))

# 여러 값 추가 (iterable)
list.extend([6, 7])
print('맨 뒤에 여러 값 추가: {}'.format(list))

# 원하는 위치에 값을 추가
# insert()
list.insert(0, 8)
print('첫 번째 자리에 8 추가함: {}'.format(list))

# 오름차순으로 정렬
# sort()
list.sort()
print('오름차순 정렬: {}'.format(list))

# 역순으로 정렬
# reverse()
list.reverse()
print('역순 정렬: {}'.format(list))
