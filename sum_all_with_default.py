# 범위의 정수를 더하는 함수 with 기본 매개변수 & 키워드 매개변수

# 함수 선언
def sum_all(start=0, end=100, step=1):
    # 변수 선언
    output = 0
    # 반복문 => 숫자 더하기
    for num in range(start, end+1, step):
        output += num

    # 리턴
    return output

# 함수 호출
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))