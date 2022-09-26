# if 조건문 & 여러 줄 문자열 (1) - 의도치 않은 들여쓰기 발생

# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문 => 짝/홀수 구분
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number, number))