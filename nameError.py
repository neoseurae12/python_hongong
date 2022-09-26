dict_key = {
    name : "7D 건조 망고",  # "name"이 아닌 name으로 쓰면 name이라는 "변수"로 인식함
    type : "당절임"         # "type"이 아닌 "type() 함수"로 인식함
}

'''
Traceback (most recent call last):
  File "d:\Workspace\python_hongong\nameError.py", line 2, in <module>
    name : "7D 건조 망고",
NameError: name 'name' is not defined
'''