# 딕셔너리 선언
from unicodedata import name


dictionary = {
    "name" : "7D 건조 당고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# 출력
print("name :", dictionary["name"])                 # name : 7D 건조 당고
print("type :", dictionary["type"])                 # type : 당절임
print("ingredient :", dictionary["ingredient"])     # ingredient : ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
print("origin :", dictionary["origin"])             # origin : 필리핀
print()


# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"])                 # name : 8D 건조 망고

# 값 - '리스트'
print(dictionary["ingredient"][1])                  # 설탕
print()

# 값 추가
print(dictionary)

print("price 값 추가 =>")
dictionary["price"] = 5000
print(dictionary)
print()

# 값 제거 - 키워드 del
del dictionary["ingredient"]
print(dictionary)