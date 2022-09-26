# 예외처리 - 1) 조건문, 2) try except 구문

# 요소 내부에 "있는" 값 찾기
numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()


# 요소 내부에 "없는" 값 찾기

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000

# 1) 조건문 ver.
print("# 조건문 ver.")
if number in numbers:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else:
    print("- 리스트 내부에 없는 값입니다.")

print()
print("--- 정상적으로 종료되었습니다. ---")

# 2) try except 구문 ver.
print("# try except 구문 ver.")
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("- 리스트 내부에 없는 값입니다.")
finally:
    print()
    print("--- 정상적으로 종료되었습니다. ---")