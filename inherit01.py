# 상속의 활용

# 부모 클래스
class Parent:
    def __init__(self) -> None:
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다")

# 자식 클래스
class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다")

# 자식 클래스의 인스턴스 생성 & 부모의 메소드 호출
child = Child()
child.test()
print(child.value)


'''
Parent 클래스의 __init()__ 메소드가 호출되었습니다
Child 클래스의 __init()__ 메소드가 호출되었습니다
Parent 클래스의 test() 메소드입니다
테스트
'''