# 조합하기
output_h = "{:+5d}".format(52)      # 기호 뒤로 밀기 & 양수        #   +52
output_i = "{:+5d}".format(-52)     # 기호 뒤로 밀기 & 음수        #   -52
output_j = "{:=+5d}".format(52)     # 기호 앞으로 밀기 & 양수      # +  52      # = 기호 : 기호 앞으로
output_k = "{:=+5d}".format(-52)    # 기호 앞으로 밀기 & 음수      # -  52
output_l = "{:+05d}".format(52)     # 0으로 채우기 & 양수          # +0052
output_m = "{:+05d}".format(-52)    # 0으로 채우기 & 음수          # -0052

output_1 = "{:=+05d}".format(52)
#output_2 = "{:=0+5d}".format(52)   # 오류 ; Invalid format => 조합 순서에 주의할 것

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print()
print("# 추가")
print(output_1)
#print(output_2)    # 오류 ; Invalid format => 조합 순서에 주의할 것