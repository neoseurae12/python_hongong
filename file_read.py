# read() 함수 => 텍스트 읽기

# 파일 열기
with open("basic.txt", "r") as file:
    # 파일 읽기 & 출력
    contents = file.read()
print(contents)