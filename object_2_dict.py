# 객체를 만드는 '함수' (1)

# 딕셔러니 리턴하는 함수
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생 리스트 선언
students = [
    create_student("마크", 87, 98, 88, 95),
    create_student("태용", 92, 98, 96, 98),
    create_student("재현", 76, 96, 94, 90),
    create_student("정우", 98, 92, 96, 92),
    create_student("해찬", 95, 98, 98, 98),
    create_student("제노", 64, 88, 92, 92)
]

# 학생 한 명씩 반복
print('이름', '총점', '평균', sep='\t')
for student in students:
    # 점수의 총합 & 평균
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_avg, sep='\t')