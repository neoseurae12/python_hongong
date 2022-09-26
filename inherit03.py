# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기

class CustomException(Exception):
    def __init__(self) -> None:
        Exception.__init__(self)
        print("#### 내가 만든 오류가 생성되었어요! ####")
    
    def __str__(self) -> str:
        return "오류가 발생했어요"

raise CustomException


'''
#### 내가 만든 오류가 생성되었어요! ####
Traceback (most recent call last):
  File "d:\Workspace\python_hongong\inherit03.py", line 11, in <module>
    raise CustomException
__main__.CustomException: 오류가 발생했어요
'''