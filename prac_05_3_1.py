numbers = [1, 2, 3, 4, 5, 6]

print("::".join(map(lambda x: str(x), numbers)))

# 답지 버전
print("::".join(map(str, numbers)))