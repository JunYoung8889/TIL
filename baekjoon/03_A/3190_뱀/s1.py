# 3190_뱀 풀이
# 2022-03-22

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 뱀 게임 함수
def game():
    # N : N * N 행렬
    N = int(input())
    # K : 사과 개수
    K = int(input())
    # apple_arr : 사과 배열
    apple_arr = [list(map(int, input().split())) for _ in range(K)]
    # L : 회전 횟수
    L = int(input())
    # turn_arr : 회전 배열
    turn_arr = [input().split() for _ in range(L)]
    # 회전 시간 int로 만들어주기 + 인덱스 에러방지
    turn_arr = [[int(i[0]),i[1]] for i in turn_arr ] + [[0,0]]
    # turn_check : 회전 순서 인덱스
    turn_check = 0
    # arr : 게임판 / 1로 감싸주기 1은 벽이나 몸을 의미
    arr = [[1]*(N+2)]+[[1]+[0]*N+[1] for _ in range(N)] + [[1]*(N+2)]
    # 시작지점 [1,1]
    i,j = 1,1
    # 몸이 있는 곳 1로 표시
    arr[i][j] = 1
    # body : 몸이 있는 칸을 표시하는 리스트
    body = [[i,j]]
    # length : 현재 몸의 길이
    length = 1
    # 델타 탐색 / 우, 하, 좌, 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 우 방향 시작
    k = 0
    # sec : 경과 시간
    sec = 0
    while True:
        # [oi,oj] : 이전 머리 위치
        oi, oj = body[length -1]
        # 회전할 시간이면
        if sec == turn_arr[turn_check][0]:
            # 회전 방향이 좌회전 이면
            if turn_arr[turn_check][1] == 'L':
                k -= 1
                # k가 -1이 되면 3으로
                if k < 0:
                    k += 4
            # 회전 방향이 우회전 이면
            else:
                k += 1
                # k가 4가 되면 0으로
                if k > 3:
                    k -= 4
            # 회전 순서 증가
            turn_check += 1
        # 다음칸 확인
        ni = oi + di[k]
        nj = oj + dj[k]
        # 시간 경과
        sec += 1
        # 머리가 벽이나 몸에 닿으면
        if arr[ni][nj] == 1:
            # 종료
            return sec
        # 머리가 사과를 발견하면
        if [ni,nj] in apple_arr:
            # 몸에 머리 위치 추가
            body.append([ni,nj])
            # 머리 위치 표시
            arr[ni][nj] = 1
            # 몸길이 증가
            length += 1
            # 사과 먹었다
            apple_arr.remove([ni,nj])
        # 머리가 사과를 발견 못하면
        else:
            # 몸에 머리 위치 추가
            body.append([ni,nj])
            # 머리 위치 표시
            arr[ni][nj] = 1
            # 몸에 이전 꼬리 위치 제거
            ki,kj = body.pop(0)
            # 이전 꼬리 위치 표시 제거 
            arr[ki][kj] = 0


print(game())