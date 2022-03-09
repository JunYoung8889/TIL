# 2178_미로_탐색 풀이
# 2022-03-09

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
arr[N-1][M-1] = 2


def my_dfs(para_arr,para_i,para_j):
    stack = []
    ans = 0
    ni = para_i
    nj = para_j
    while True:
        stack.append([ni,nj])
        ans += 1
        para_arr[ni][nj] = 3
        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni += di
            nj += dj
            if 0 <= ni < N and 0 <= nj < M and para_arr[ni][nj] != 0 and para_arr[ni][nj] != 3:
                if para_arr[ni][nj] == 2:
                    return ans
                break
            else:
                ni -= di
                nj -= dj
        else:
            ni, nj = stack.pop()
            ans -= 1



print(my_dfs(arr,0,0)+1)