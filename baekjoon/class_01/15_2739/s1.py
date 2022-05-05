# 2739_구구단 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for n in range(1, 10):
    print(N, '*', n, '=', N * n)