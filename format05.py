output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)      # 15칸
output_c = "{:+15f}".format(52.273)     # 15칸 & 부호 추가
output_d = "{:+015f}".format(52.273)    # 15칸 & 부호 추가 & 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)