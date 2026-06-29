# slice 방식으로 리스트 수정

# n~n 구간 리스트 수정
list1 = [0, 1, 2, 3, 4, 5]
list1[1:4] = [11, 22, 33]

# n~n 구간 리스트 삭제
list2 = [0, 1, 2, 3, 4, 5]
del(list2[1:4])

print('list1: {}, list2: {}'.format(list1, list2))