# 테이블에 나눠 앉히기

min_sit = 2
max_sit = 10
everyone = 100
memo = {}

def familyRestaurantSeat(remain, sitted):
    key = str([remain, sitted])

    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0    # 무효
    if remain == 0:
        return 1    # 유효
    
    # 재귀 처리
    count = 0
    for i in range(sitted, max_sit+1):
        count += familyRestaurantSeat(remain-i, i)

    # 메모화 처리
    memo[key] = count

    # 종료
    return count

print(familyRestaurantSeat(everyone, min_sit))

'''
437420
'''