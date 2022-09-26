# Getter & Setter

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

    # Getter & Setter
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0 :
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value


# 원의 둘레 & 넓이
circle = Circle(10)
print("# 원의 둘레 & 넓이")
print("원의 둘레: {}".format(circle.get_circumference()))
print("원의 넓이: {}".format(circle.get_area()))
print()

# getter & setter => 간접적으로 프라이빗 변수 __radius에 접근
print("# __radius에 접근")
print(circle.get_radius())
print()

# 반지름을 변경 -> 원의 둘레 & 넓이
print("# 반지름 변경 -> 원의 둘레 & 넓이")
circle.set_radius(2)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())