# 1436_영화감독-숌 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
for i in range(666, int(1e7)):
    if '666' in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break