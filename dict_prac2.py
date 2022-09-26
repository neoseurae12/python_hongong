# p.171 - 딕셔너리와 리스트의 조합

# 딕셔너리의 리스트 선언
from ctypes import sizeof


pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

print("# 우리 동네 애완 동물")
for i in range(len(pets)) :
    output = "{} {}살".format(pets[i].get("name"), pets[i].get("age"))  # .format() 기능 사용
    print(output)
print()

# 답지 ver.
for pet in pets :
    print(pet["name"], str(pet["age"]) + "살")
print()


'''
# 우리 동네 애완 동물
구름 5살
초코 3살
아지 1살
호랑이 1살
'''