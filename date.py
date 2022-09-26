# 날짜/시간과 관련된 기능을 가져옵니다
import datetime

# 현재 날짜/시간을 구합니다
now = datetime.datetime.now()

# 출력
print(now.year, "년")       # 2022 년
print(now.month, "월")      # 3 월
print(now.day, "일")        # 22 일
print(now.hour, "시")       # 17 시
print(now.minute, "분")     # 5 분
print(now.second, "초")     # 1 초