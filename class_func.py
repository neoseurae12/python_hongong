# 클래스 함수

# 클래스 선언
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("--------학생 목록--------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------- -------- --------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

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


# 학생 리스트 선언
Student("마크", 87, 98, 88, 95)
Student("태용", 92, 98, 96, 98)
Student("재현", 76, 96, 94, 90)
Student("정우", 98, 92, 96, 92)
Student("해찬", 95, 98, 98, 98)
Student("제노", 64, 88, 92, 92)
Student("천러", 82, 86, 98, 88)
Student("지성", 88, 74, 78, 92)
Student("런쥔", 97, 92, 88, 95)
Student("샤오쥔", 45, 52, 72, 78)

# 현재 생성된 학생들 모두 출력
Student.print()


'''
--------학생 목록--------
이름    총점    평균
마크    368     92.0
태용    384     96.0
재현    356     89.0
정우    378     94.5
해찬    389     97.25
제노    336     84.0
천러    354     88.5
지성    332     83.0
런쥔    372     93.0
샤오쥔  247     61.75
-------- -------- --------
'''