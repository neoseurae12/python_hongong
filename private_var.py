# 프라이빗 변수 (private variable)

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


# 원의 둘레 & 넓이
circle = Circle(10)
print("원의 둘레: {}".format(circle.get_circumference()))
print("원의 넓이: {}".format(circle.get_area()))
print()

# 프라이빗 변수 __radius에 접근
print("# __radius에 접근")
print(circle.__radius)


'''
원의 둘레: 62.83185307179586
원의 넓이: 314.1592653589793

# __radius에 접근
AttributeError: 'Circle' object has no attribute '__radius' => 오류 발생
'''