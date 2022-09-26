# '함수 데코레이터'의 기본

# 함수 데코레이터 생성
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    
    return wrapper

# 데코레이터를 붙여 함수 만들기
@test
def hello():
    print("hello")

# 함수 호출
hello()