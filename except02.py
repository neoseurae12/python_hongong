# "여러" 종류의 예외가 발생할 수 있는 코드

# 변수 선언
list_number = [52, 273, 32, 72, 100]

# 예외 처리 - try except 구문
try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)


'''
정상적으로 정수 입력한 경우

정수 입력 > 2
2번째 요소: 32
'''

'''
정수로 변환될 수 없는 값 입력한 경우

type(exception): <class 'ValueError'>
exception: invalid literal for int() with base 10: 'yes!'
'''

'''
정수지만 리스트의 길이를 넘는 인덱스를 입력한 경우

type(exception): <class 'IndexError'>
exception: list index out of range
'''