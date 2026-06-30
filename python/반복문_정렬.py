# 선택 정렬
a = [3,4,10,5,1]

for i in range(0, 5):
    for j in range(i+1, 5):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

for k in a:
    print(k, end=' ')

print()

# 버블 정렬
b = [3, 4, 10, 5, 1]
n = len(b)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

for x in b:
    print(x, end=' ')