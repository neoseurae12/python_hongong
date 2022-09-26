# 범위 내부의 정수를 모두 더하는 함수

# 함수 선언
def sum_all(start, end):
    # 변수 선언
    output = 0
    # 반복문 => 숫자 더하기
    for num in range(start, end+1):
        output += num

    # 리턴
    return output

# 함수 호출
print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))

'''
0 to 100: 5050
0 to 1000: 500500
50 to 100: 3825
500 to 1000: 375750
'''