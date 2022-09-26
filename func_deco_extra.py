# 함수 데코레이션 - functools 모듈 사용 / 매개변수 전달로 소스의 가독성 높이기

# 모듈 가져오기
from functools import wraps

# 함수로 데코레이터 생성
def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        print("인사가 시작되었습니다.")
        function(*arg, **kwargs)
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello(name1, name2):
    print("hello, {} and {}".format(name1, name2))

hello("마크", "해찬")

'''
인사가 시작되었습니다.
hello, 마크 and 해찬
인사가 종료되었습니다.
'''

# 뭐야 교재 그대로 했는데 에러 뜸... => 교재에서 indent를 잘못한 듯
# 솔직히 '함수 데코레이터' 뭔 소리인지 감 잘 안 옴. => https://dojang.io/mod/page/view.php?id=2427 참고할 것