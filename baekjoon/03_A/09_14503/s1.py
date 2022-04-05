# 14503_로봇-청소기 풀이
# 2022-04-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 로봇 청소기 함수 구현하기
def robot(N, M, arr):
    global r, c, d, ans
    # 0북, 1동, 2남, 3서
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    # 출발지 초기화
    oi, oj = r, c
    while True:
        # 현재 위치를 청소한다.
        arr[oi][oj] = 2
        nd = d
        while True:
            # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
            if nd == d-4:
                # 바라보는 방향을 유지한 채로 한칸 후진
                oi -= di[d]
                oj -= dj[d]
                # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우
                if arr[oi][oj] == 1:
                    # 작동을 멈춘다.
                    return
                # 회전탐색 종료
                break
            # 왼쪽 탐색
            ni = oi + di[(nd-1)%4]
            nj = oj + dj[(nd-1)%4]
            # 인덱스 범위를 만족하면
            if 0 <= ni < N and 0 <= nj < M:
                # 청소하지 않은 공간이 존재하면
                if arr[ni][nj] == 0:
                    oi = ni
                    oj = nj
                    # 그 방향으로 회전 전진
                    d = (nd-1)%4
                    # 회전탐색 종료
                    break
            # 왼쪽으로 회전
            nd -= 1


# arr : N * M 행렬
N, M = map(int, input().split())
# r,c 출발점 / d 출발 방향
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 로봇 청소기 작동
robot(N, M, arr)
# 청소가 완료된 구역 개수 초기화
ans = 0
# 2차원 탐색
for i in range(N):
    for j in range(M):
        # 2는 청소가 완료된 구역을 의미
        if arr[i][j] == 2:
            ans += 1
print(ans)