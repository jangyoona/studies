import datetime

my_1st = datetime.datetime(2026, 6, 29)
print(my_1st)


# 시간까지 포함
def datetime_my_dating():
    first_day = datetime.datetime(2025, 6, 29)
    dating = datetime.datetime.now() - first_day
    return dating

print("{}일".format(datetime_my_dating()))


# 날짜 기준으로 일 수만 계산 (int 반환)
def days_my_dating():
    first_day = datetime.date(2025, 6, 29)
    dating = datetime.date.today() - first_day
    return dating.days
print("{}일".format(days_my_dating()))