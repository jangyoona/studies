def add(x, y):
    return x + y
def sub(x, y):
    return x - y


number1 = [1, 2, 3, 4]
number2 = [5, 6, 7, 8]

result1 = list(map(add, number1, number2))
# result2 = list(map(lambda x, y: x+y, number1, number2))

result2 = list(map(sub, number2, number1))
# result2 = list(map(lambda x, y: x - y, number2, number1))

print(result1)
print(result2)