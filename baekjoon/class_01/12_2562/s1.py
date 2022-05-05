# 2562_최댓값 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')
arr = [int(input()) for _ in range(9)]
max_num = 0
max_idx = 0
for n in range(9):
    if arr[n] > max_num:
        max_num = arr[n]
        max_idx = n
print(max_num)
print(max_idx + 1)