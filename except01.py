# 예외 객체

# 예외 처리 - try except 구문
try:
    number_input_a = int(input("정수 입력 > "))
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", number_input_a*number_input_a*3.14)
except Exception as exception:
    # 예외 객체 출력
    print("type(exception):", type(exception))
    print("exception:", exception)

'''
정수 입력 > yes
type(exception): <class 'ValueError'>
exception: invalid literal for int() with base 10: 'yes'
'''