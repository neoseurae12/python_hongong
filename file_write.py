# 랜덤하게 1000명의 키와 몸무게 데이터 만들기

# 랜덤한 숫자 생성
import random

# 간단한 한글 리스트 생성
hanguls = list("가나다라마바사아자차카타파하")

# 파일 '쓰기' 모드
with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 쓰기
        file.write("{}, {}, {}\n".format(name, weight, height))