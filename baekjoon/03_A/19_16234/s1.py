# 16234_인구-이동 풀이
# 2022-04-20
# python3 : 7592ms / pypy3 : 916ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 이동 함수 구현
def move(arr):
    global N, L, R, ans
    # 방문 확인 리스트
    visited = [[0]*N for _ in range(N)]
    # 이동 후 배열
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[i][j]
    # bfs
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue = [(i,j)]
                front = -1
                rear = 0
                visited[i][j] = 1
                while front != rear:
                    front += 1
                    oi, oj = queue[front]
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni = oi + di
                        nj = oj + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if visited[ni][nj] == 0:
                                # 인구 차이가 L이상 R이하이면 이동 가능
                                if L <= abs(arr[ni][nj] - arr[oi][oj]) <= R:
                                    queue.append((ni,nj))
                                    rear += 1
                                    visited[ni][nj] = 1
                # 연합 수, 합 계산
                union_sum = 0
                union_cnt = 0
                for ui, uj in queue:
                    union_sum += arr[ui][uj]
                    union_cnt += 1
                change_num = int(union_sum / union_cnt)
                # 연합 인구 갱신
                for ci, cj in queue:
                    new_arr[ci][cj] = change_num
    # 모든 탐색을 마치고 이동이 없으면
    if new_arr == arr:
        return False
    # 이동이 있으면
    else:
        # 인구 이동 배열 갱신
        for i in range(N):
            for j in range(N):
                arr[i][j] = new_arr[i][j]
        return True


# N*N 행렬 / 차이가 L 이상 R 이하이면 국경 오픈
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# ans 경과된 날짜
ans = 0
while True:
    # 이동이 있으면
    if move(arr):
        ans += 1
    # 이동이 없으면
    else:
        break
print(ans)