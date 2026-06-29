# comprehension
# zip()? 두 개 이상의 리스트나 스트링을 받아서 인덱스에 맞게 자료를 묶어줌.

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {x : y for x, y in zip(product_list, price_list)}

print(product_dict)

students = ["태연", "진우", "정현", "하늘", "성진"]
print({"{}번".format(number):name for number, name in enumerate(students)})