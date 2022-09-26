# 10진수 <-> 2진수
dec_to_bin = "{:b}".format(10)
print(dec_to_bin)
'''1010'''

bin_to_dec = int("1010", 2)
print(bin_to_dec)
'''10'''

# 10진수 <-> 8진수
dec_to_oct = "{:o}".format(10)
print(dec_to_oct)
'''12'''

oct_to_dec = int("12", 8)
print(oct_to_dec)
'''10'''

# 10진수 <-> 16진수
dec_to_hex = "{:x}".format(10)
print(dec_to_hex)
'''a'''

hex_to_dec = int("a", 16)
print(hex_to_dec)