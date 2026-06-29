# for문 > list
numbers= [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# for문 > range 응용
# range(10): 0~9 / range(5, 10): 5~9
for number in range(10):
    print(number)

# for문 > enumerate
# 리스트의 경우 순서(index)와 값을 반환한다.
names = ['장', '쑤', '성']
for i, value in enumerate(names):
    print('{}번째 글자는? "{}"'.format(i, value))


print('=================================================')

# for문 list(반복가능한_객체) map(함수, 반복가능한_객체) lambda - 익명함수
testList = [1, 2, 3, 4, 5]
testList = list(map(lambda num : num + 100, testList)) # lambda
# testList = [i + 100 for i in testList]                 # comprehension
print(testList)