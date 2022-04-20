# 16235_나무-재테크 풀이
# 2022-04-20
# python3 : 시간초과 / pypy3 : 888ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 1년 함수 구현하기
def year():
    global N, Arr, tree_idx, garden_arr, land_arr, ans, visited
    for ti, tj in tree_idx:
        garden_arr[ti][tj].sort(reverse=True)
        death = 0
        for idx in range(len(garden_arr[ti][tj])-1,-1,-1):
            # 봄
            if land_arr[ti][tj] - garden_arr[ti][tj][idx] >= 0:
                land_arr[ti][tj] -= garden_arr[ti][tj][idx]
                garden_arr[ti][tj][idx] += 1
            # 여름
            else:
                death += garden_arr[ti][tj].pop(idx)//2
        land_arr[ti][tj] += death
    # 가을
    new_tree = []
    for ti, tj in tree_idx:
        for tree in garden_arr[ti][tj]:
            if tree%5 == 0:
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    ni = ti + di
                    nj = tj + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        garden_arr[ni][nj] += tuple([1])
                        if visited[ni][nj] == 0:
                            new_tree.append((ni,nj))
                            visited[ni][nj] = 1
    # 겨울
    tree_idx += new_tree
    for i in range(N):
        for j in range(N):
            land_arr[i][j] += Arr[i][j]


# N*N 사이즈 / M 그루 나무 시작 / K년 경과
N, M, K = map(int, input().split())
# 양분 배열
Arr = [list(map(int, input().split())) for _ in range(N)]
# 트리 배열
tree_arr = [list(map(int, input().split())) for _ in range(M)]
# 트리 위치
tree_idx = []
# 트리 방문 리스트
visited = [[0]*N for _ in range(N)]
# 화단 나무 성장 상태
garden_arr = [[[] for __ in range(N)] for _ in range(N)]
for ti, tj, tn in tree_arr:
    garden_arr[ti-1][tj-1] += [tn]
    tree_idx.append((ti-1, tj-1))
    visited[ti-1][tj-1] = 1

# 땅 양분 상태
land_arr = [[5]*N for _ in range(N)]
# K년 경과
for _ in range(K):
    year()

# 나무 개수 세기
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(garden_arr[i][j])
print(ans)