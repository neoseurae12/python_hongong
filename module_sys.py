# sys 모듈

# 모듈 읽어들이기
import sys

# 명령 매개변수 출력
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보 출력
print("getwindowsversion():", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램 강제 종료
sys.exit()


'''
C:\Users\Wonhui Roh>python d:/Workspace/python_hongong/module_sys.py 10 20 30
['d:/Workspace/python_hongong/module_sys.py', '10', '20', '30']
---
getwindowsversion(): sys.getwindowsversion(major=10, minor=0, build=22000, platform=2, service_pack='')
---
copyright: Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
---
version: 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
'''