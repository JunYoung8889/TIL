# 2304_창고_다각형 풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-i-1):
        if arr[j][0] > arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

max_val = 0
max_idx = 0
for i in range(N):
    if arr[i][1] > max_val:
        max_val = arr[i][1]
        max_idx = i
ans = max_val
h = 0
for i in range(max_idx):
    if arr[i][1] > h:
        h = arr[i][1]
    ans += (arr[i+1][0] - arr[i][0]) * h
h = 0
for i in range(N-1,max_idx,-1):
    if arr[i][1] > h:
        h = arr[i][1]
    ans += (arr[i][0] - arr[i-1][0]) * h
print(ans)

