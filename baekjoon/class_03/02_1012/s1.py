# 1012_유기농-배추 풀이
# 2022-05-28

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 네트워크 문제 dfs로 구현하기
def dfs(i, j):
    global arr, N, M, visited
    visited[i][j] = 1
    stack = [(i, j)]
    top = 0
    while stack:
        oi, oj = stack[top]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = oi + di
            nj = oj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))
                    top += 1
                    break
        else:
            stack.pop()
            top -= 1
    return


# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # N행 M열 배추 K개
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                cnt += 1
    print(cnt)