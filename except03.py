# 예외 처리를 했지만 예외를 못 잡는 경우

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


'''
Traceback (most recent call last):
  File "d:\Workspace\python_hongong\except03.py", line 10, in <module>
    예외.발생해주세요()
NameError: name '예외' is not defined
'''