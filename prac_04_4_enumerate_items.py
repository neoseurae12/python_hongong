# enumerate() 함수 & items() 함수

# 리스트 & enumerate() 함수
list_original = [81, 82, 83, 84]
list_enumerate = enumerate(list_original)

# 출력 - '튜플' 형태
#for element in list_enumerate:
#    print(element)
'''
(0, 81)
(1, 82)
(2, 83)
(3, 84)
'''

# 출력 - '튜플' 활용 
#for i, v in list_enumerate:
#    print("인덱스 : {}, 값 : {}".format(i, v))
'''
인덱스 : 0, 값 : 81
인덱스 : 1, 값 : 82
인덱스 : 2, 값 : 83
인덱스 : 3, 값 : 84
'''

# 딕셔너리 & items()
dict_original = {"music" : "beatbox", "singer" : "nctdream", "leader" : "mark"}
dict_items = dict_original.items()

# 출력 - '튜플' 형태
for item in dict_items:
    print(item)
'''
('music', 'beatbox')
('singer', 'nctdream')
('leader', 'mark')
'''