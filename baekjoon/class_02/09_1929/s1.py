# 1929_소수-구하기 풀이
# 2022-05-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# M이상 N이하 소수 찾기
# 에라토스테네스의 체
M, N = map(int, input().split())
for num in range(M, N+1):
    if num == 1:
        continue
    # num의 제곱근까지 탐색해도 충분
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        print(num)