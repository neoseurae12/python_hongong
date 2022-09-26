# 키가 존재하는지 확인 -> 값에 접근

# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# 입력 받기 from 사용자
key = input("> 접근하고자 하는 키 : ")

# 출력 - 키워드 'in' 사용
if key in dictionary :
    print(dictionary[key])
else :
    print("존재하지 않는 키에 접근하고 있습니다.")