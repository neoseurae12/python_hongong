# reversed() 함수 & 이터레이터

# 변수 선언
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers 출력
print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))


'''
6
5
4
3
2
'''