# 7569_토마토 풀이
# 2022-03-12

import sys
sys.stdin = open('input.txt', 'r')

def bfs(para_arr, N, M, H):
    for n in range(N+M+H):
        for h in range(H):
            for i in range(N):
                for j in range(M):
                    if para_arr[h][i][j] != 0 and para_arr[h][i][j] != -1:
                        for dh, di, dj in [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]:
                            if 0 <= h+dh < H and 0 <= i+di < N and 0 <= j+dj < M:
                                if para_arr[h+dh][i+di][j+dj] == 0:
                                    para_arr[h+dh][i+di][j+dj] = para_arr[h][i][j] + 1
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