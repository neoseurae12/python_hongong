# os 모듈

# 모듈 읽어들이기
import os

# 기본 정보 몇 개 출력
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더 생성 & 제거 (폴더가 비어있을 때만 제거 가능)
#os.mkdir("hello")
#os.rmdir("hello")

# 파일 생성 & 파일 이름 변경
# with open("original.txt", 'w') as file:
#     file.write("hello")
# os.rename("original.txt", "new.txt")

# 파일 제거
#os.remove("new.txt")
# os.unlink("new.txt")

# 시스템 명령어 실행
os.system("dir")



'''
현재 운영체제: nt
현재 폴더: D:\Workspace\python_hongong
현재 폴더 내부의 요소: ['array_comprehensions.py', 'basic.txt', 'boolean.py', 'break.py', 'break01.py', 'call_with_func.py', 'circle.py', 'cmpop_range.py', 'cmpop_string.py', 'condition.py', 'condition01.py', 'condition02.py', 'condition05.py', 'condition06.py', 'condition_ex.py', 'D2Coding-Ver1.3.2-20180524', 'date.py', 'date01.py', 'date02.py', 'date03.py', 'default_param.py', 'destructive.py', 'dict01.py', 'dict02.py', 'dict03.py', 'dict_prac2.py', 'dict_prac3.py', 'dict_prac4.py', 'enumerate.py', 'ex01.py', 'except01.py', 'except02.py', 'except03.py', 'except_all.py', 'except_as.py', 'except_multi.py', 'extend.py', 'factorial_for.py', 'factorial_recursion.py', 'false_value.py', 'fibonacci_memo.py', 'fibonacci_recursion.py', 'fibonacci_recursion02.py', 'fibonacci_recursion03.py', 'file_closed01.py', 'file_closed02.py', 'file_closed03.py', 'file_closed04.py', 'file_open.py', 'file_read.py', 'file_readlines.py', 'file_write.py', 'finally_loop.py', 'format01.py', 'format02.py', 'format03.py', 'format04.py', 'format05.py', 'format06.py', 'format07.py', 'format_basic.py', 'format_ex.py', 'for_dict.py', 'for_ex2.py', 'for_ex4.py', 'for_ex5.py', 'for_list.py', 'for_list01.py', 'for_list_ex.py', 'for_range.py', 'func_as_param.py', 'fun_basic.py', 'generator.py', 'generator01.py', 'get01.py', 'handle_with_condition.py', 'handle_with_try.py', 'hello.py', 'if_else_ex.py', 'if_string.py', 'if_string01.py', 'if_string02.py', 'in.py', 'inch.py', 'index_error.py', 'infinite_loop.py', 'info.txt', 'input.py', 'input_error.py', 'int_convert.py', 'int_float01.py', 'int_float02.py', 'in_not in.py', 'is__.py', 'items.py', 'iterator01.py', 'key_in.py', 'lambda01.py', 'lambda02.py', 'list01.py', 'list02.py', 'list03.py', 'list_in.py', 'list_op_double.py', 'list_op_internal.py', 'list_range01.py', 'module_os.py', 'module_random.py', 'module_sys.py', 'nameError.py', 'output.py', 'param_basic.py', 'param_examples.py', 'param_keyword01.py', 'param_TypeError.py', 'pass_keyword01.py', 'prac_02_1_3.py', 'prac_02_1_4.py', 'prac_02_1_5.py', 'prac_04_3_2.py', 'prac_04_3_3.py', 'prac_04_3_4.py', 'prac_04_4_count.py', 'prac_04_4_dec_oct_hex.py', 'prac_04_4_enumerate_items.py', 'prac_05_1_1_1.py', 'prac_05_1_1_2.py', 'prac_05_1_2.py', 'prac_05_2_1.py', 'prac_05_2_2.py', 'prac_05_3_1.py', 'prac_05_3_2.py', 'prac_06_1_2.py', 'remove.py', 'return_none.py', 'return_only.py', 'return_with_data.py', 'reversed.py', 'reversed_for01.py', 'reversed_for02.py', 'sample.py', 'split.py', 'str.py', 'string01.py', 'string02.py', 'string03.py', 'string_operator.py', 'string_operator01.py', 'string_operator02.py', 'strip.py', 'sum_all_basic.py', 'sum_all_with_default.py', 'swap.py', 'test.txt', 'try_except_else.py', 'try_except_else_finally.py', 'try_pass.py', 'try_return01.py', 'try_return02.py', 'tuple_basic.py', 'tuple_divmod.py', 'tuple_return.py', 'tuple_use01.py', 'tuple_use02.py', 'upper_ex.py', 'upper_lower.py', 'variable.py', 'variable_param.py', 'while_as_for.py', 'while_with_condition.py', 'while_with_time.py']
 Volume in drive D is New Volume
 Volume Serial Number is 6688-4A1D

 Directory of D:\Workspace\python_hongong

07/11/2022  04:23 PM    <DIR>          .
06/29/2022  01:25 AM    <DIR>          ..
06/23/2022  03:06 PM               220 array_comprehensions.py
07/07/2022  12:06 PM                28 basic.txt      
03/22/2022  04:46 PM               148 boolean.py     
06/22/2022  12:11 PM               269 break.py       
06/22/2022  12:14 PM               243 break01.py     
06/30/2022  07:42 PM               658 call_with_func.py
03/03/2022  04:39 PM               196 circle.py      
03/22/2022  04:42 PM                63 cmpop_range.py 
03/22/2022  04:35 PM               172 cmpop_string.py
03/22/2022  04:59 PM               272 condition.py   
03/22/2022  05:30 PM               355 condition01.py
03/22/2022  05:35 PM               220 condition02.py 
03/22/2022  05:52 PM               464 condition05.py 
03/22/2022  06:05 PM               598 condition06.py 
03/22/2022  05:43 PM               272 condition_ex.py
02/14/2022  12:50 AM    <DIR>          D2Coding-Ver1.3.2-20180524
03/22/2022  05:06 PM               389 date.py        
03/22/2022  05:10 PM               350 date01.py      
03/22/2022  05:15 PM               437 date02.py      
03/22/2022  05:19 PM               678 date03.py      
06/27/2022  12:38 PM               207 default_param.py
03/29/2022  03:48 PM               372 destructive.py 
06/20/2022  10:24 AM             1,076 dict01.py      
06/20/2022  10:27 AM               367 dict02.py      
06/20/2022  10:32 AM               404 dict03.py      
06/22/2022  12:21 PM               670 dict_prac2.py  
06/20/2022  11:12 AM               303 dict_prac3.py  
06/20/2022  11:34 AM               815 dict_prac4.py  
06/23/2022  02:54 PM             1,054 enumerate.py   
02/14/2022  10:47 AM               136 ex01.py        
07/08/2022  06:23 PM               558 except01.py    
07/09/2022  07:49 PM               833 except02.py    
07/09/2022  07:55 PM               841 except03.py    
07/09/2022  07:57 PM               947 except_all.py  
07/09/2022  07:53 PM               507 except_as.py   
07/09/2022  07:51 PM               399 except_multi.py
03/29/2022  03:45 PM               149 extend.py      
06/28/2022  01:26 PM               353 factorial_for.py
06/28/2022  01:27 PM               283 factorial_recursion.py
03/22/2022  06:14 PM               404 false_value.py 
06/28/2022  01:52 PM               546 fibonacci_memo.py
06/28/2022  01:40 PM               480 fibonacci_recursion.py
06/28/2022  01:46 PM               836 fibonacci_recursion02.py
06/28/2022  01:47 PM               959 fibonacci_recursion03.py
07/08/2022  03:04 PM               318 file_closed01.py
07/08/2022  03:05 PM               337 file_closed02.py
07/08/2022  03:06 PM               348 file_closed03.py
07/08/2022  03:16 PM               342 file_closed04.py
07/07/2022  12:09 PM               373 file_open.py   
07/07/2022  12:11 PM               167 file_read.py   
07/07/2022  12:46 PM             1,229 file_readlines.py
07/07/2022  12:22 PM               545 file_write.py  
07/08/2022  06:02 PM               489 finally_loop.py
03/10/2022  05:48 PM               354 format01.py    
03/10/2022  05:59 PM               639 format02.py    
03/10/2022  06:30 PM               474 format03.py    
03/10/2022  07:05 PM               941 format04.py    
03/10/2022  07:06 PM               301 format05.py    
03/18/2022  06:30 PM               242 format06.py    
03/18/2022  06:34 PM               123 format07.py    
03/10/2022  05:44 PM               137 format_basic.py
03/22/2022  04:17 PM               222 format_ex.py   
06/20/2022  10:51 AM               338 for_dict.py    
03/31/2022  06:44 PM               147 for_ex2.py     
03/31/2022  06:46 PM               146 for_ex4.py     
03/31/2022  06:49 PM               145 for_ex5.py     
03/31/2022  06:35 PM               177 for_list.py    
06/23/2022  03:02 PM               234 for_list01.py  
03/31/2022  06:37 PM                95 for_list_ex.py 
06/22/2022  11:33 AM               250 for_range.py   
06/30/2022  07:31 PM               295 func_as_param.py
06/27/2022  12:18 PM               217 fun_basic.py   
07/07/2022  12:47 PM               226 generator.py   
07/07/2022  12:52 PM               458 generator01.py 
06/20/2022  10:47 AM               575 get01.py       
07/08/2022  02:43 PM               527 handle_with_condition.py
07/08/2022  02:46 PM               379 handle_with_try.py
02/14/2022  12:58 AM                28 hello.py       
03/22/2022  06:29 PM               382 if_else_ex.py  
06/23/2022  03:16 PM               457 if_string.py   
06/23/2022  03:16 PM               443 if_string01.py 
06/23/2022  03:18 PM               448 if_string02.py 
03/22/2022  04:05 PM                93 in.py
03/03/2022  04:36 PM               133 inch.py        
03/18/2022  06:44 PM               179 index_error.py 
06/22/2022  11:56 AM               266 infinite_loop.py
07/08/2022  03:09 PM                 0 info.txt       
03/03/2022  03:56 PM               139 input.py       
03/03/2022  04:02 PM               206 input_error.py 
03/03/2022  04:27 PM               266 int_convert.py 
03/03/2022  04:09 PM               116 int_float01.py 
03/03/2022  04:11 PM               279 int_float02.py 
03/31/2022  06:28 PM                95 in_not in.py   
03/22/2022  04:01 PM                71 is__.py        
06/23/2022  02:58 PM               530 items.py       
06/27/2022  11:36 AM               307 iterator01.py  
06/20/2022  10:38 AM               519 key_in.py      
06/30/2022  07:46 PM               607 lambda01.py    
06/30/2022  07:48 PM               938 lambda02.py    
03/27/2022  12:25 AM               613 list01.py      
03/27/2022  12:37 AM               356 list02.py      
03/31/2022  06:04 PM               686 list03.py      
06/23/2022  03:03 PM               127 list_in.py     
03/27/2022  12:09 AM               117 list_op_double.py
03/27/2022  12:12 AM               108 list_op_internal.py
06/22/2022  11:36 AM               196 list_range01.py
07/11/2022  04:24 PM               600 module_os.py   
07/11/2022  03:53 PM             1,282 module_random.py
07/11/2022  04:10 PM             1,057 module_sys.py  
05/10/2022  04:31 PM               392 nameError.py   
02/14/2022  11:53 AM               516 output.py      
06/27/2022  12:20 PM               238 param_basic.py 
06/28/2022  12:47 PM               421 param_examples.py
06/28/2022  12:45 PM               767 param_keyword01.py
06/27/2022  12:24 PM               753 param_TypeError.py
03/22/2022  06:22 PM               282 pass_keyword01.py
07/10/2022  09:18 PM               104 prac_02_1_3.py 
07/10/2022  09:24 PM               359 prac_02_1_4.py 
07/10/2022  09:26 PM               175 prac_02_1_5.py 
06/22/2022  12:26 PM               184 prac_04_3_2.py 
06/22/2022  12:32 PM               400 prac_04_3_3.py 
06/22/2022  12:38 PM               352 prac_04_3_4.py 
06/27/2022  12:15 PM               828 prac_04_4_count.py
06/27/2022  12:04 PM               425 prac_04_4_dec_oct_hex.py
06/27/2022  11:57 AM               797 prac_04_4_enumerate_items.py
06/28/2022  01:10 PM                43 prac_05_1_1_1.py
06/28/2022  01:12 PM                52 prac_05_1_1_2.py
06/28/2022  01:13 PM               134 prac_05_1_2.py 
06/30/2022  02:51 PM               382 prac_05_2_1.py 
06/30/2022  05:42 PM               623 prac_05_2_2.py 
07/07/2022  01:15 PM               136 prac_05_3_1.py 
07/07/2022  01:08 PM               347 prac_05_3_2.py 
07/08/2022  06:13 PM               987 prac_06_1_2.py 
03/31/2022  06:08 PM                68 remove.py      
06/28/2022  12:54 PM               142 return_none.py 
06/28/2022  12:51 PM               185 return_only.py 
06/28/2022  12:53 PM               136 return_with_data.py
06/23/2022  02:41 PM               711 reversed.py    
06/22/2022  11:49 AM               132 reversed_for01.py
06/22/2022  11:50 AM               137 reversed_for02.py
02/14/2022  12:46 AM               107 sample.py      
03/22/2022  04:08 PM                77 split.py       
03/03/2022  04:32 PM               108 str.py
06/23/2022  03:25 PM               892 string01.py    
06/23/2022  03:30 PM               553 string02.py    
06/23/2022  03:34 PM               493 string03.py    
02/14/2022  04:54 PM               132 string_operator.py
02/14/2022  05:07 PM               204 string_operator01.py
02/14/2022  05:09 PM               207 string_operator02.py
03/22/2022  03:53 PM               265 strip.py       
06/28/2022  01:04 PM               443 sum_all_basic.py
06/28/2022  01:08 PM               445 sum_all_with_default.py
03/03/2022  04:45 PM               189 swap.py        
07/08/2022  05:58 PM                 0 test.txt       
07/08/2022  02:53 PM               374 try_except_else.py
07/08/2022  02:59 PM               469 try_except_else_finally.py
07/08/2022  02:50 PM               434 try_pass.py
07/08/2022  03:16 PM               780 try_return01.py
07/08/2022  05:58 PM               448 try_return02.py
06/30/2022  07:13 PM               134 tuple_basic.py 
06/30/2022  07:28 PM               136 tuple_divmod.py
06/30/2022  07:24 PM               170 tuple_return.py
06/30/2022  07:17 PM               399 tuple_use01.py 
06/30/2022  07:22 PM               224 tuple_use02.py 
03/22/2022  04:21 PM               276 upper_ex.py    
03/18/2022  06:52 PM               192 upper_lower.py 
02/16/2022  12:53 PM               192 variable.py    
06/27/2022  12:28 PM               493 variable_param.py
06/22/2022  11:58 AM               140 while_as_for.py
06/22/2022  12:02 PM               205 while_with_condition.py
06/22/2022  12:09 PM               332 while_with_time.py
             170 File(s)         63,686 bytes
               3 Dir(s)  491,109,478,400 bytes free  
'''