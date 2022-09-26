a = input("문자열 입력> ")
b = input("문자열 입력> ")

print(a, b)
print()

# 단순한 방법 
print(b, a)
print()

# swap을 이용한 방법
a, b = b, a
print(a, b)