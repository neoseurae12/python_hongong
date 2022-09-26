# 파일 "한 줄씩" 읽기 <- 반복문

with open("info.txt", "r") as file:
    for line in file:
        # 변수 선언
        (name, weight, height) = line.strip().split(", ")

        # 데이터의 문제 체기 ; 문제 있을 시 지나감
        if (not name) or (not weight) or (not height):
            continue

        # 결과 계산
        bmi = int(weight) / (int(int(height) / 100) ** 2)
        result = ""
        
        if bmi >= 25:
            result = "과체중"
        elif bmi >=18.5:
            result = "정상 체중"
        else:
            result = "저체중"
        
        # 출력
        # print("이름: {}".format(name))
        # print("몸무게: {}".format(weight))
        # print("키: {}".format(height))
        # print("BMI: {}".format(bmi))
        # print("결과: {}".format(result))
        # print()

        # 출력 - 문자열의 join() 함수 ; 문자열.join(문자열로 구성된 리스트) - p.203
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()