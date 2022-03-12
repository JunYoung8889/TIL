# 2178_미로 탐색 풀이
# 2022-03-12

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 최단거리 문제는 bfs 풀면 쉽다!
def bfs(para_arr, para_i, para_j):
    # bfs는 queue로 구현하면 쉽다!
    queue = [[para_i,para_j]]
    # queue가 빌 때까지 진행!
    while queue:
        # queue는 선입선출! FIFO!
        oi, oj = queue.pop(0)
        # 델타탐색 상, 하, 좌, 우!
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            # new i,j / old i,j
            ni = oi + di
            nj = oj + dj
            # 새로 탐색할 인덱스가 인덱스 범위를 만족하면
            if 0 <= ni < N and 0 <= nj < M:
                # 해당 인덱스의 값이 1이면
                if para_arr[ni][nj] == 1:
                    # queue에 노드를 추가!
                    queue.append([ni,nj])
                    # 해당 인덱스 값을 거리로 표시!
                    para_arr[ni][nj] = para_arr[oi][oj] + 1

# N * M 행렬
N, M = map(int,input().split())
# arr : N * M 크기의 미로 배열
arr = [list(map(int,input())) for _ in range(N)]
# 0,0에서 bfs 출발
bfs(arr,0,0)
# N-1,M-1이 도착지점이므로 해당 도착지까지의 최단거리가 표기됨
print(arr[N-1][M-1])