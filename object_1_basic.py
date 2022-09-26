# 딕셔너리로 '객체' 만들기

# 학생 리스트

students = [
    {"name": "마크", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "태용", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "재현", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "정우", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "해찬", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "제노", "korean": 64, "math": 88, "english": 92, "science": 92}
]

# 학생 한 명씩 반복

print("이름", "총점", "평균", sep='\t')

for student in students:
    # 점수의 총합 & 평균
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_avg, sep='\t')