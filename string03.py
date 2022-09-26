# 구문 내부에 여러 줄 문자열 - 해결법_2) 문자열의 join() 함수

# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문 => 짝/홀수 구분
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.", 
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))