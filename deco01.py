# 데코레이터를 사용한 Getter & Setter

# 모듈
import math

# 클래스 선언
class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # Getter & Setter -- 데코레이터 사용 버전
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0 :
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value


# 원의 둘레 & 넓이
print("# 데코레이터를 사용한 Getter & Setter")
circle = Circle(10)
print("원래 원의 반지름: {}".format(circle.radius))
circle.radius = 2
print("변경된 원의 반지름: {}".format(circle.radius))
print()

# 강제로 예외 발생
print("# 강제로 예외 발생")
circle.radius = -10


'''
# 데코레이터를 사용한 Getter & Setter
원래 원의 반지름: 10
변경된 원의 반지름: 2

# 강제로 예외 발생
TypeError: 길이는 양의 숫자여야 합니다.
'''