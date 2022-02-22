# 2559_수열 풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = list(map(int, input().split()))
small = 0
for i in range(K):
    small += arr[i]
ans = small
for i in range(K,N):
    small += arr[i] - arr[i-K]
    if small > ans:
        ans = small
print(ans)