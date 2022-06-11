# 2230_수-고르기 풀이
# 2022-06-11

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

min_ans = int(1e9)
for i in range(N-1):
    for j in range(i+1, N):
        ans = abs(arr[i] - arr[j])
        if ans == M:
            print(M)
            sys.exit()
        if ans > M and ans < min_ans:
            min_ans = ans
print(min_ans)