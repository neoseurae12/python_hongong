# 람다

# 함수 선언 with lambda(람다)
power = lambda x: x * x
under_3 = lambda x: x < 3

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)    # 제너레이터
print("map(power, list_input_a):", list(output_a))

# filter() 함수
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("# filter(under_3, list_output_a):", output_b)    # 제너레이터
print("# filter(under_3, list_output_a):", list(output_b))