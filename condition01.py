# 입력
number = input("정수 입력 > ")

# 마지막 자리 숫자 추출
last_char = number[-1]

# 숫자로 변환
last_num = int(last_char)

# 짝수 확인
if last_num % 2 == 0 :
    print("짝수입니다")

# 홀수 확인
if last_num % 2 != 0 :
    print("홀수입니다")

# 참고 : \ => 줄바꿈해서 코드 입력 가능