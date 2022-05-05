# 2439_별-찍기-2 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for n in range(N):
    print(' ' * (N-n-1) + '*' * (n+1))