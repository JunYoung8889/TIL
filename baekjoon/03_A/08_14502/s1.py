# 14502_연구소 풀이
# 2022-04-02

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# n C 3으로 벽 만드는 함수 구현하기
def make_wall(now_wall_list, now_wall_cnt):
    global safe_zone_list, safe_zone_cnt, make_wall_list
    # 3개 다 뽑았으면
    if now_wall_cnt == 3:
        make_wall_list.append(now_wall_list[:])
        return
    # 덜 뽑았으면
    else:
        for i in range(safe_zone_cnt):
            # 이 코드 세줄을 넣으면 조합이 만들어지고
            # 이 코드 세줄을 안넣으면 순열이 만들어진다.
            if now_wall_cnt != 0:
                if safe_zone_list[i] <= now_wall_list[-1]:
                    continue
            # [:] 슬라이싱으로 얕은복사를 막아주자
            if safe_zone_list[i] not in now_wall_list:
                make_wall(now_wall_list[:] + [safe_zone_list[i]], now_wall_cnt + 1)
        return


# 바이러스 확인하는 함수 구현하기
def virus_check(N, M, arr, wall3):
    global max_safe_zone, virus_list
    global wall_cnt, virus_cnt
    # 방문 리스트 초기화
    visited = [[0]*M for _ in range(N)]
    # 벽3개 방문처리
    for i, j in wall3:
        visited[i][j] = 1
    # bfs는 queue로 구현하자
    queue = virus_list[:]
    # 처음 출발지 방문처리
    for i, j in queue:
        visited[i][j] = 1
    # 머리, 꼬리 초기화
    front = -1
    rear = virus_cnt-1
    # 현재까지 퍼진 바이러스 수
    now_virus_cnt = 0
    # front == rear는 queue가 비었음을 의미
    while front != rear:
        # 큐는 머리에서 뽑아온다.
        front += 1
        oi, oj = queue[front]
        # 바이러스 퍼진 카운트 증가
        now_virus_cnt += 1
        # 가지치기
        if now_virus_cnt >= N*M - max_safe_zone - wall_cnt -3:
            return
        # 델타탐색 / 상, 하, 좌, 우
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni = oi + di
            nj = oj + dj
            # 인덱스 범위를 만족하고 방문한적 없으면
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                # 통로이면
                if arr[ni][nj] == 0:
                    # 큐는 꼬리에 추가한다.
                    queue.append((ni,nj))
                    rear += 1
                    visited[ni][nj] = 1
    # 탐색 완료했으면 최대치 계산해서 갱신
    max_safe_zone = N*M - now_virus_cnt - wall_cnt -3
    return


# arr : N * M 행렬
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 안전지대 좌표 리스트
safe_zone_list = []
# 안전지대 개수
safe_zone_cnt = 0
# 벽 개수
wall_cnt = 0
# 바이러스 좌표 리스트
virus_list = []
# 바이러스 개수
virus_cnt = 0
for i in range(N):
    for j in range(M):
        # 안전지대이면
        if arr[i][j] == 0:
            safe_zone_list.append((i,j))
            safe_zone_cnt += 1
        # 벽이면
        elif arr[i][j] == 1:
            wall_cnt += 1
        # 바이러스이면
        else:
            virus_list.append((i,j))
            virus_cnt += 1
# 벽3개 세우기 좌표 리스트
make_wall_list = []
# n C 3 함수
make_wall([],0)
# 최대 안전지대 개수 초기화
max_safe_zone = 0
# 벽3개 세운 뒤
for wall3 in make_wall_list:
    # 바이러스 퍼진 장소를 체크해서
    # 최대 안전지대 개수를 계산하자
    virus_check(N, M, arr, wall3)
print(max_safe_zone)