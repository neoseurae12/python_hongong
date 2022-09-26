# 예외 처리 - 1) 조건문

# 숫자 입력 받기
user_input_a = input("정수 입력 > ")

# 조건문 & .isdigit() 함수 => 사용자 입력이 '숫자'로만 구성되어 있을 때
if user_input_a.isdigit():
    # 숫자로 변환
    number_input_a = int(user_input_a)
    # 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", number_input_a*number_input_a*3.14)
else:
    print("정수를 입력하지 않았습니다.")