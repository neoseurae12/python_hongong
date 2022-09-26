# 현재 디렉터리를 읽어 들이고 '파일'인지 '디렉터리(폴더)'인지 구분하기

# 모듈 읽어들이기
import os

# 현재 폴더의 파일/폴더 출력
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더 구분
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)