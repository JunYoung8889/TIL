# 7569_토마토 풀이
# 2022-03-12

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 최단거리 문제는 bfs로 풀자!
def bfs():
    # bfs는 queue로 구현하자!
    queue = []
    # front : 머리 / queue는 머리에서 뽑는다.
    front = -1
    # rear : 꼬리 / queue는 꼬리에 쌓는다.
    rear = -1
    # arr : N행 * M열 * H층 행렬
    M, N, H = map(int, input().split())
    arr = []
    for h in range(H):
        tmp = []
        for i in range(N):
            tmp.append(list(map(int, input().split())))
            for j in range(M):
                if tmp[i][j] == 1:
                    # queue에 쌓으면 꼬리는 하나 증가
                    queue.append([h,i,j])
                    rear += 1
        arr.append(tmp)

    # 머리와 꼬리가 같아지면 queue가 비었다는 소리!
    while front != rear:
        # 큐에서 뽑을때는 머리가 하나 증가
        front += 1
        oh, oi, oj = queue[front]
        # 델타탐색 6방향 상, 하, 좌, 우, 윗층, 아랫층
        for dh, di, dj in [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]:
            nh = oh + dh
            ni = oi + di
            nj = oj + dj
            # 인덱스 범위를 만족하면
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                # 아직 방문 안한 곳 이면
                if arr[nh][ni][nj] == 0:
                    arr[nh][ni][nj] = arr[oh][oi][oj] + 1
                    # queue에 쌓으면 꼬리는 하나 증가
                    queue.append([nh, ni, nj])
                    rear += 1

    max_num = 0
    for h in arr:
        for i in h:
            for j in i:
                if j == 0:
                    return -1
                if j > max_num:
                    max_num = j
    # 걸린 날짜 : 최대값 - 1 ( 1에서 시작했으므로 )
    return max_num - 1


print(bfs())