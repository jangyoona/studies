li = ['Apple', 'Banana', 'Cherry']
cnt = 0
str = ' '

for i in li:
    for j in i:
        str += j[0]
        cnt = cnt + 1

        if cnt > 5:
            break

print(f'cnt: {cnt}, str: {str}')

