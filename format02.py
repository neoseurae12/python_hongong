# 정수
output_a = "{:d}".format(52)    # {:d} => int 자료형의 정수 출력을 직접 지정. only 정수만 매개변수로 올 수 있음.

# 특정 칸에 출력하기 ; 뒤에서부터 숫자 채움
output_b = "{:5d}".format(52)   # 5칸
output_c = "{:10d}".format(52)  # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)  # 양수
output_e = "{:05d}".format(-52) # 음수  # 맨 앞자리 => 부호

print("# 기본")
print(output_a)
print()
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print()
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)