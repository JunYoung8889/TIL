# 7569_토마토 풀이
# 2022-03-12

import sys
sys.stdin = open('input.txt', 'r')

def bfs(para_arr, N, M, H):
    queue = []
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if para_arr[h][i][j] == 1:
                    queue.append([h,i,j])
    while queue:
        oh, oi, oj = queue.pop(0)
        for dh, di, dj in [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]:
            nh = oh + dh
            ni = oi + di
            nj = oj + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                if para_arr[nh][ni][nj] == 0:
                    para_arr[nh][ni][nj] = para_arr[oh][oi][oj] + 1
                    queue.append([nh, ni, nj])
    max_num = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if para_arr[h][i][j] == 0:
                    return -1
                if para_arr[h][i][j] > max_num:
                    max_num = para_arr[h][i][j]
    return max_num - 1


M, N, H = map(int, input().split())
arr = []
for h in range(H):
    arr.append([list(map(int, input().split())) for _ in range(N)])

print(bfs(arr,N,M,H))