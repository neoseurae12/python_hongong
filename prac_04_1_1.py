# 리스트(list)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)   # extend() : 한 번에 '여러' 요소 추가
print("extend():", list_a)
'''
extend(): [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
'''

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.append(10)   # append() : 요소 '하나' 추가 - 리스트 '뒤쪽'에
print("append():", list_a)
'''
append(): [0, 1, 2, 3, 4, 5, 6, 7, 10]
'''

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.insert(3, 0) # insert() : 요소 '하나' 추가 - 리스트 '특정 위치'에
print("insert():", list_a)
'''
insert(): [0, 1, 2, 0, 3, 4, 5, 6, 7]
'''

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.remove(3)    # remove() : '값'으로 제거하기
print("remove():", list_a)
'''
remove(): [0, 1, 2, 4, 5, 6, 7]
'''

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.pop(3)   # pop() : '인덱스'로 제거하기 (del 키워드와 동일)
print("pop():", list_a)
'''
pop(): [0, 1, 2, 4, 5, 6, 7]
'''

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.clear()  # clear() : 모두 제거하기
print("clear():", list_a)
'''
clear(): []
'''