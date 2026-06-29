# comprehension

areas1 = [ i*i for i in range(1,11) ]                          # [ 계산식 for문 ]
areas2 = [ i*i for i in range(1,11) if i % 2 == 0]             # [ 계산식 for문 조건문 ]
areas3 = [ ( x, y ) for x in range(15) for y in range(15) ]    # [ 계산식 for문 for문 ]



# 1부터 100 사이의 8의 배수 추출하여 저장하기
arr = [i for i in range(1, 101) if i % 8 == 0]
print(arr)


print('=======================================')
# 기출문제 중 lambda를 컴프리헨션으로
test_list = [1, 2, 3, 4, 5]
# test_list = list(map(lambda num : num + 100, test_list))
test_list = [num + 100 for num in test_list]

for i in test_list:
    print(i, end=' ')