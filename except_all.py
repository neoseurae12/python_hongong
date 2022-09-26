# 모든 예외 잡기

# 변수 선언
list_number = [52, 273, 32, 72, 100]

# 예외 처리 - try except 구문
try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    # ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)
except Exception as exception:
    # 이외의 예외가 발생하는 경우
    print("미리 파악하지 못한 예외가 발생했습니다")
    print("exception:", exception)


'''
정수 입력 > 2
2번째 요소: 32
미리 파악하지 못한 예외가 발생했습니다
exception: name '예외' is not defined
'''