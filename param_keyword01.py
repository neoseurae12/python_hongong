# 키워드 매개변수

def print_n_times(*values, n=2):
    # n => n번 반복
    for i in range(n):
        # values => 리스트처럼 활용
        for value in values:
            print(value)
        print()


# 의도치 않은 출력 결과
print_n_times("안녕하세요", "이상한", "파이썬 프로그래밍", 3)

'''
안녕하세요
이상한
파이썬 프로그래밍
3

안녕하세요
이상한
파이썬 프로그래밍
3

'''

# 의도한 출력 결과
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

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