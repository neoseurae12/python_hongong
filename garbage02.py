# 가비지 컬렉터: 변수에 저장한 경우

class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성(init)".format(self.name))
    
    def __del__(self):
        print("{} - 파괴(del)".format(self.name))


a = Test("A")
b = Test("B")
c = Test("C")

'''
A - 생성(init)
B - 생성(init)
C - 생성(init)
A - 파괴(del)
B - 파괴(del)
C - 파괴(del)
'''