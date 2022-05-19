# 2156_포두주-시식 풀이
# 2022-05-14
# python3 : 452ms / pypy3 : 160ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt' , 'r')

# 입력 받기
N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
# 1인 경우 dp 만들 필요 없음
if N == 1:
    print(arr[N])
# 1이 아닌경우 dp 만들기
else:
    dp = [0]*(N+1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + arr[i], dp[i-1], dp[i-3] + arr[i-1] + arr[i])
    print(dp[N])