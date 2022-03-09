# 10157_자리배정 풀이
# 2022-02-26

import sys
sys.stdin = open('input.txt', 'r')

C, R = map(int, input().split())
K = int(input())
arr = [[1]+[0]*R+[1] for _ in range(C)]
arr = [[1]*(R+2)] + arr + [[1]*(R+2)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
ni = 1
nj = 1
k = 0
arr[ni][nj] = 1
num = 2
if K > R * C:
    print(0)
else:
    while num < K+1:
        if arr[ni+di[k]][nj+dj[k]] == 0:
            arr[ni][nj] = num
            ni += di[k]
            nj += dj[k]
        else:
            k = (k+1)%4
            continue
        num += 1
    print(ni, nj)