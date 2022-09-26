# 리스트 선언
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)   # [1, 2, 3, 4, 5]
print()

# 리스트 중간에 요소 추가
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)    # [10, 1, 2, 3, 4, 5]
print(list_a)