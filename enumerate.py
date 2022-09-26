# enumerate() 함수 & 리스트

# 변수 선언
example_list = ["요소A", "요소B", "요소C"]

# 출력 - 그냥 쌩
print("# 단순 출력")
print(example_list)
print()

# 출력 - enumerate() 함수 적용
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# 출력 - list() 함수로 강제 변환
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문 & enumerate() 함수 조합해서 사용
print("# 반복문 & emerate() 함수 조합")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))


'''
# 단순 출력
['요소A', '요소B', '요소C']

# enumerate() 함수 적용 출력
<enumerate object at 0x00000206B8E19100>

# list() 함수로 강제 변환 출력
[(0, '요소A'), (1, '요소B'), (2, '요소C')]

# 반복문 & emerate() 함수 조합
0번째 요소는 요소A입니다.
1번째 요소는 요소B입니다.
2번째 요소는 요소C입니다.
'''