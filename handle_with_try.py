# 예외 처리 - 2) try except 구문

# try except 구문
try:
    # 숫자로 변환
    number_input_a = int(input("정수 입력 > "))
    # 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", number_input_a*number_input_a*3.14)
except:
    print("무언가 잘못되었습니다.")