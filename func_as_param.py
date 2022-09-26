# 함수의 매개변수로 '함수' 전달하기

# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 전달할 함수
def print_hello():
    print("안녕하십니까")

# 조합
call_10_times(print_hello)