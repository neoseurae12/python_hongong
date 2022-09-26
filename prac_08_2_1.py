# 크기 비교 함수

# 클래스
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __eq__(self, value) -> bool:
        return self.get_avg() == value

    def __ne__(self, value) -> bool:
        return self.get_avg() != value

    def __gt__(self, value):
        return self.get_avg() > value
    
    def __ge__(self, value):
        return self.get_avg() >= value

    def __lt__(self, value):
        return self.get_avg() < value
    
    def __le__(self, value):
        return self.get_avg() <= value


# 학생 선언
test = Student("A", 90, 90, 90, 90)

# 출력
print("test == 90 =", test == 90)
print("test != 90 =", test != 90)
print("test > 90 =", test > 90)
print("test >= 90 =", test >= 90)
print("test < 90 =", test < 90)
print("test <= 90 =", test <= 90)


'''
test == 90 = True
test != 90 = False
test > 90 = False
test >= 90 = True
test < 90 = False
test <= 90 = True
'''