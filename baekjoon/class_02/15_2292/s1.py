# 2292_벌집 풀이
# 2022-05-28

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 1 ≤ N ≤ 1,000,000,000
N = int(input())

# 규칙성 찾아서 구현하기!
check_num = 1
cnt = 1
while True:
    if N > check_num:
        check_num += 6*cnt
        cnt += 1
    # 발견
    else:
        print(cnt)
        break