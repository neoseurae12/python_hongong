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

    def __str__(self) -> str:
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )

    def __eq__(self, value) -> bool:
        return self.get_sum == value.get_sum()

    def __ne__(self, value) -> bool:
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

    
# 학생 리스트 선언
students = [
    Student("마크", 87, 98, 88, 95),
    Student("태용", 92, 98, 96, 98),
    Student("재현", 76, 96, 94, 90),
    Student("정우", 98, 92, 96, 92),
    Student("해찬", 95, 98, 98, 98),
    Student("제노", 64, 88, 92, 92)
]

# 학생 선언
student_a = Student("마크", 87, 98, 88, 95)
student_b = Student("태용", 92, 98, 96, 98)

# 출력
print("student_a == student_b =", student_a.__eq__(student_b))
print("student_a != student_b =", student_a.__ne__(student_b))
print("student_a > student_b =", student_a.__gt__(student_b))
print("student_a >= student_b =", student_a.__ge__(student_b))
print("student_a < student_b =", student_a.__lt__(student_b))
print("student_a <= student_b =", student_a.__le__(student_b))


'''
student_a == student_b = False
student_a != student_b = True
student_a > student_b = False
student_a >= student_b = False
student_a < student_b = True
student_a <= student_b = True
'''