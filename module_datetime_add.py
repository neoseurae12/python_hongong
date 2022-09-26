# datetime 모듈 => 시간 처리하기

# 모듈 읽어들이기
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print()

# 특정 시간 이후의 시간 구하기 => datetime.timedelta() -- ※ '년(年)' 단위의 연산은 불가!
print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print()

# 특정 시간 요소 교체하기 => now.replace() -- 특히 '년(年)' 단위
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))


'''
2022년 07월 15일 17시 47분 03초

# datetime.timedelta로 시간 더하기
2022년 07월 23일 18시 48분 04초

# now.replace()로 1년 더하기
2023년 07월 15일 17시 47분 03초
'''