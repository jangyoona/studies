# 같은 인스턴스인지? is
# 같은 값인지? ==

list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")


# target이 특정 클래스의 인스턴스인지 확인
# isinstance(target, type)
list3 = list(range(10))
list4 = [1, 2, 3]

if isinstance(list3, list) and isinstance(list4, list):
    print('list3과 list4는 둘 다 list 클래스 입니다.')