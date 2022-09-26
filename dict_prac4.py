print(type("문자열") is str)
print(type([]) is list)
print(type({}) is dict)
print()

# 딕셔너리 선언
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반복문 사용
for key in character:
    element = character[key]
    #print(element)
    #print(type(element))
    if (type(element) is str) or (type(element) is int):
        print("{} : {}".format(key, element))
    elif (type(element) is dict):
        for k in element:
            print("{} : {}".format(k, element[k]))
    elif (type(element) is list):
        for i in range(len(element)):
            print("{} : {}".format(key, element[i]))