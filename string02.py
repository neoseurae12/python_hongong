# 구문 내부에 여러 줄 문자열 - 해결법_1) 괄호로 문자열 연결 (2)

# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문 => 짝/홀수 구분
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number, number))

# 마지막 문자열까지도 \n을 입력하는 "실수" 하지 말 것