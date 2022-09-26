# reversed() 함수

# 리스트 선언 & 뒤집기
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) : ", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])) : ", list(list_reversed))
print()

# 반복문 적용
print("# reversed() 함수 & 반복문")
print("for i in reversed([1, 2, 3, 4, 5]) : ")
for i in reversed(list_a) : 
    print("-", i)

'''
# reversed() 함수
reversed([1, 2, 3, 4, 5]) :  <list_reverseiterator object at 0x000002424D332FD0>
list(reversed([1, 2, 3, 4, 5])) :  [5, 4, 3, 2, 1]

# reversed() 함수 & 반복문
for i in reversed([1, 2, 3, 4, 5]) : 
- 5
- 4
- 3
- 2
- 1
'''