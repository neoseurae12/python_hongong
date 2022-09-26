# 딕셔너리의 items() 함수 & 반복문

# 변수 선언
example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

# 딕셔너리의 items() 함수 결과 출력
print("# 딕셔너리의 items() 함수")
print("items() :", example_dictionary.items())
print()

# for 반복문 & items() 함수 조합하여 사용
print("# 딕셔너리의 items() 함수 & 반복문 조합")

for key, element in example_dictionary.items() :
    print("dictionary[{}] = {}".format(key, element))