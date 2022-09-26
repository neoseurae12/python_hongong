# "인라인" 람다

# 함수 선언 with lambda(람다)
#power = lambda x: x * x
#under_3 = lambda x: x < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수
output_a = map(lambda x: x*x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)    # 제너레이터
print("map(power, list_input_a):", list(output_a))

# filter() 함수
output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행결과")
print("# filter(under_3, list_output_a):", output_b)    # 제너레이터
print("# filter(under_3, list_output_a):", list(output_b))

'''
# map() 함수의 실행결과
map(power, list_input_a): <map object at 0x000001D6D65E4FA0>
map(power, list_input_a): [1, 4, 9, 16, 25]
# filter() 함수의 실행결과
# filter(under_3, list_output_a): <filter object at 0x000001D6D65E4E80>
# filter(under_3, list_output_a): [1, 2]
'''