# 리스트나 문자열에서 여러개의 값을 가져오기
# slice 기능

rainbow = ['빨', '주', '노', '초', '파', '남', '보']

# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[0:3]

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[4:]

print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))



# 함수 변형
def substring(text, start, end):
    return text[start:end]

text = 'Hello world'
between_2_5 = substring(text, 2, 5)
print(between_2_5)


# 인자 3개 활용
# list[시작값:끝값:step] 형식으로 step값을 주어 그 값만큼 건너뛰어 가져올 수 있음

list2 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list2[5:15:3]

print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list2[17:4:-4]

print(reverse_list)