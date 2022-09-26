list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1] - del 키워드
del list_a[1]
print("del list_a[1] :", list_a)    # [0, 2, 3, 4, 5]

# 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2) :", list_a)           # [0, 2, 4, 5]

list_a.pop()
print("pop() :", list_a)            # [0, 2, 4]

# del 키워드 - 범위 지정
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print(list_b)                       # [0, 1, 2, 6]

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print(list_c)                       # [3, 4, 5, 6]

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
print(list_d)                       # [0, 1, 2]