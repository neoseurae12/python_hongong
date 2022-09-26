# 클래스 변수

# 클래스 선언

class Student:
    count = 0

    def __init__(self, name, korean, math, english, science) -> None:
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다".format(Student.count))


# 학생 리스트 선언

students = [
    Student("마크", 87, 98, 88, 95),
    Student("태용", 92, 98, 96, 98),
    Student("재현", 76, 96, 94, 90),
    Student("정우", 98, 92, 96, 92),
    Student("해찬", 95, 98, 98, 98),
    Student("제노", 64, 88, 92, 92)
]

# 출력
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))