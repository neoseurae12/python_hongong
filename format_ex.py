a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")

print("{} + {} = {}".format(a, b, int(a) + int(b)))
# 단순히 a+b 해버리면 '정수의 덧셈'이 아닌, '문자열의 concatenate'가 되어버림