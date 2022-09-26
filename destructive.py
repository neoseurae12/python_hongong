# 리스트 연결 연산자 : +
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)  # [1, 2, 3, 4, 5, 6]
print(list_a)           # [1, 2, 3]
print(list_b)           # [4, 5, 6]

# 요소 추가 : append(), insert(), extend()
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)   # [1, 2, 3, 4, 5, 6]
print(list_b)   # [4, 5, 6]