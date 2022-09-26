# 5초 동안 반복하기

# '시간'과 관련된 기능 가져오기
import time

number = 0

# 5초 동안 반복
target_tick = time.time() + 5
while time.time() < target_tick :
    number += 1

# 출력
print("5초 동안 {}번 반복했습니다.".format(number))


# '통신'할 때 자주 사용하는 코드