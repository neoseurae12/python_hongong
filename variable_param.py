# 가변 매개변수 함수

def print_n_times(n, *values):
    # n => n번 반복
    for i in range(n):
        # values => '리스트'처럼 활용
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

'''
안녕하세요
즐거운
파이썬 프로그래밍

안녕하세요
즐거운
파이썬 프로그래밍

안녕하세요
즐거운
파이썬 프로그래밍

'''