# 피보나치 수열 - 재귀 함수 ver. - 3 => UnboundLocalError 예외 발생

# 변수 선언
counter = 0

def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력
    #print("fibonacci({})를 구합니다.".format(n))
    #global counter
    counter += 1

    # 피보나치 수
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print("fibonacci(1):", fibonacci(1))
# print("fibonacci(2):", fibonacci(2))
# print("fibonacci(3):", fibonacci(3))
# print("fibonacci(4):", fibonacci(4))
# print("fibonacci(5):", fibonacci(5))

print("fibonacci(10):", fibonacci(10))
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}입니다.".format(counter))

#print("fibonacci(35):", fibonacci(50))  # 너무 오래 걸림 (거의 1시간 이상)

'''
UnboundLocalError: local variable 'counter' referenced before assignment
'''