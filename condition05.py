# 날짜/시간과 관련된 기능 가져오기
import datetime

# 현재 날짜/시간
# 쉽게 사용할 수 있게 월을 변수에 저장
now = datetime.datetime.now()
month = now.month

# 조건문 => 계절 확인
if 3 <= month <= 5 :
    print("현재는 봄입니다")
elif 6 <= month <= 8 :
    print("현재는 여름입니다")
elif 9 <= month <= 11 :
    print("현재는 가을입니다")
else :
    print("현재는 겨울입니다")