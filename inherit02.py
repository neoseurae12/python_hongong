# 사용자 정의 예외 클래스 만들기

class CustomException(Exception):
    def __init__(self) -> None:
        Exception.__init__(self)

# raise로 예외 발생시키기
raise CustomException

'''
__main__.CustomException
'''