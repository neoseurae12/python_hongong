# 딕셔너리에 요소 '제거'하기

# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

# 출력 - before
print("요소 제거 이전 : ", dictionary)

# 딕셔너리 요소 '제거'
del dictionary["name"], dictionary["type"]
#del dictionary["name"]
#del dictionary["type"]

# 출력 - after
print("요소 제거 이후 : ", dictionary)