# 범위의 매개변수

# 매개변수 1개 - range(A) : 0 ~ (A-1)의 정수
para1 = range(10)
print(list(para1))
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# 매개변수 2개 - range(A, B) : A ~ (B-1)의 정수
para2 = range(3, 10)
print(list(para2))
'''
[3, 4, 5, 6, 7, 8, 9]
'''

# 매개변수 3개 - range(A, B, C) : A ~ (B-1)의 정수 with C의 간격
para3 = range(0, 100, 10)
print(list(para3))
'''
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
'''