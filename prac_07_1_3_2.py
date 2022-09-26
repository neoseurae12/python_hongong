# 폴더라면 또 탐색하기 -- 재귀 구성

# 모듈 읽어들이기
import os

# 폴더를 읽어들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        # 폴더 => 계속 읽어들이기
        if os.path.isdir(item):
            read_folder(item)
        # 파일 => 출력
        else:
            print("파일:", item)

# 현재 폴더의 파일/폴더 출력
read_folder(".")


'''
파일: array_comprehensions.py
파일: basic.txt
파일: boolean.py
파일: break.py
파일: break01.py
파일: call_with_func.py
파일: circle.py
파일: cmpop_range.py
파일: cmpop_string.py
파일: condition.py
파일: condition01.py
파일: condition02.py
파일: condition05.py
파일: condition06.py
파일: condition_ex.py
파일: D2Coding
파일: D2CodingAll
파일: D2CodingLigature
파일: date.py
파일: date01.py
파일: date02.py
파일: date03.py
파일: default_param.py
파일: destructive.py
파일: dict01.py
파일: dict02.py
파일: dict03.py
파일: dict_prac2.py
파일: dict_prac3.py
파일: dict_prac4.py
파일: enumerate.py
파일: ex01.py
파일: except01.py
파일: except02.py
파일: except03.py
파일: except_all.py
파일: except_as.py
파일: except_multi.py
파일: extend.py
파일: factorial_for.py
파일: factorial_recursion.py
파일: false_value.py
파일: fibonacci_memo.py
파일: fibonacci_recursion.py
파일: fibonacci_recursion02.py
파일: fibonacci_recursion03.py
파일: file_closed01.py
파일: file_closed02.py
파일: file_closed03.py
파일: file_closed04.py
파일: file_open.py
파일: file_read.py
파일: file_readlines.py
파일: file_write.py
파일: finally_loop.py
파일: format01.py
파일: format02.py
파일: format03.py
파일: format04.py
파일: format05.py
파일: format06.py
파일: format07.py
파일: format_basic.py
파일: format_ex.py
파일: for_dict.py
파일: for_ex2.py
파일: for_ex4.py
파일: for_ex5.py
파일: for_list.py
파일: for_list01.py
파일: for_list_ex.py
파일: for_range.py
파일: func_as_param.py
파일: fun_basic.py
파일: generator.py
파일: generator01.py
파일: get01.py
파일: handle_with_condition.py
파일: handle_with_try.py
파일: hello.py
파일: if_else_ex.py
파일: if_string.py
파일: if_string01.py
파일: if_string02.py
파일: in.py
파일: inch.py
파일: index_error.py
파일: infinite_loop.py
파일: info.txt
파일: input.py
파일: input_error.py
파일: int_convert.py
파일: int_float01.py
파일: int_float02.py
파일: in_not in.py
파일: is__.py
파일: items.py
파일: iterator01.py
파일: key_in.py
파일: lambda01.py
파일: lambda02.py
파일: list01.py
파일: list02.py
파일: list03.py
파일: list_in.py
파일: list_op_double.py
파일: list_op_internal.py
파일: list_range01.py
파일: module_datetime.py
파일: module_datetime_add.py
파일: module_os.py
파일: module_random.py
파일: module_sys.py
파일: module_time.py
파일: module_urllib.py
파일: nameError.py
파일: output.py
파일: param_basic.py
파일: param_examples.py
파일: param_keyword01.py
파일: param_TypeError.py
파일: pass_keyword01.py
파일: prac_02_1_3.py
파일: prac_02_1_4.py
파일: prac_02_1_5.py
파일: prac_04_3_2.py
파일: prac_04_3_3.py
파일: prac_04_3_4.py
파일: prac_04_4_count.py
파일: prac_04_4_dec_oct_hex.py
파일: prac_04_4_enumerate_items.py
파일: prac_05_1_1_1.py
파일: prac_05_1_1_2.py
파일: prac_05_1_2.py
파일: prac_05_2_1.py
파일: prac_05_2_2.py
파일: prac_05_3_1.py
파일: prac_05_3_2.py
파일: prac_06_1_2.py
파일: prac_07_1_3_1.py
파일: prac_07_1_3_2.py
파일: remove.py
파일: return_none.py
파일: return_only.py
파일: return_with_data.py
파일: reversed.py
파일: reversed_for01.py
파일: reversed_for02.py
파일: sample.py
파일: split.py
파일: str.py
파일: string01.py
파일: string02.py
파일: string03.py
파일: string_operator.py
파일: string_operator01.py
파일: string_operator02.py
파일: strip.py
파일: sum_all_basic.py
파일: sum_all_with_default.py
파일: swap.py
파일: test.txt
파일: try_except_else.py
파일: try_except_else_finally.py
파일: try_pass.py
파일: try_return01.py
파일: try_return02.py
파일: tuple_basic.py
파일: tuple_divmod.py
파일: tuple_return.py
파일: tuple_use01.py
파일: tuple_use02.py
파일: upper_ex.py
파일: upper_lower.py
파일: variable.py
파일: variable_param.py
파일: while_as_for.py
파일: while_with_condition.py
파일: while_with_time.py
'''