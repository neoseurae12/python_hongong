# 매개변수와 관련된 TypeError

def print_n_times(value, n):
    for i in range(n):
        print(value)

# 매개변수를 '덜' 넣은 경우
#print_n_times("안녕하세요")
'''
Traceback (most recent call last):
  File "d:\Workspace\python_hongong\param_TypeError.py", line 8, in <module>
    print_n_times("안녕하세요")
TypeError: print_n_times() missing 1 required positional argument: 'n'
'''

# 매개변수를 '더' 넣은 경우
print_n_times("안녕하세요", 10, 20)
'''
Traceback (most recent call last):
  File "d:\Workspace\python_hongong\param_TypeError.py", line 17, in <module>
    print_n_times("안녕하세요", 10, 20)
TypeError: print_n_times() takes 2 positional arguments but 3 were given
'''