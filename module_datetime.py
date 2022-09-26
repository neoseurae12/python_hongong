# datetime 모듈

# 모듈 읽어들이기
import datetime

# 현재 시간 구하기 & 출력
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# 시간 출력 방법
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, \
                                                 now.month, \
                                                 now.day, \
                                                 now.hour, \
                                                 now.minute, \
                                                 now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))

print(output_a)
print(output_b)
print(output_c)


'''
# 현재 시각 출력하기
2022 년
7 월
15 일
17 시
36 분
58 초

# 시간을 포맷에 맞춰 출력하기
2022.07.15 17:36:58
2022년 7월 15일 17시 36분 58초
2022년 07월 15일 17시 36분 58초
'''