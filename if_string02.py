# if 조건문 & 긴 문자열 (3) - 문자열을 한 줄로 길게 적으면 코드가 복잡해지는 문제 발생

# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문 => 짝/홀수 구분
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))