# isinstance() 함수 활용

# 학생 클래스
class Student:
    def study(self):
        print('공부합니다')

# 선생님 클래스
class Teacher:
    def teach(self):
        print('가르칩니다')

# 교실 내부의 객체 리스트
stranger = None
classroom = [Student(), Student(), Teacher(), Student(), Student(), stranger]

# 반복 => 적절한 함수 호출 <- isinstance() 함수
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
    else:
        print('누구세요')