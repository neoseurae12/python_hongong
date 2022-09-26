# 팩토리얼 계산 - for 반복문 ver.

def factorial(n):
    output = n

    for num in range(n-1, 1-1, -1):
        #print(num)
        output *= num
        #print(output)
    
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))