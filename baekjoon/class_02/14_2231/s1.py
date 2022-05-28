# 2231_분해합 풀이
# 2022-05-28

# 파일 불러오기
import sys
sys.stdin = open('input.txt' , 'r')

# N : 자연수
N = int(input())

# 검사 해야될 최소 범위 계산
min_num = N-len(str(N))*9
if min_num < 0:
    min_num = 0

# 분해합 검사
for n in range(min_num, N+1):
    total = n
    for s in str(n):
        total += int(s)
    
    # 생성자 발견
    if total == N:
        print(n)
        break

# 생성자가 없으면
else:
    print(0)