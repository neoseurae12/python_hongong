# 파일 열고 닫기

# 파일 열기
file = open("basic.txt", "w")

# 파일에 텍스트 write
file.write("Hello Python Programming...!")

# 파일 닫기
file.close()

'''
'with 키워드'로 실수 방지하기

# 파일 열기
with open("basic.txt", "w") as file:
    # 파일에 텍스트 write
    file.write("Hello Python Programming...!")
'''
