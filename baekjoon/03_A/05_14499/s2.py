# 14499_주사위-굴리기 풀이
# 2022-03-24

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N * M 행렬
# 초기위치 (x,y) / (i,j)
# 명령 개수 K
N, M , x, y, K = map(int, input().split())
# arr : 지도
arr = [list(map(int, input().split())) for _ in range(N)]
# 명령 리스트
command_list = list(map(int, input().split()))

# 주사위 상태 초기화 6면 각 0으로 초기화
dice = [0]*6
# 전개도 초기 상태
# 북 2 남 5 서 4 동 3 윗면 1 바닥 6 으로 시작
up, down, left, right, top, bottom = 2, 5, 4, 3, 1, 6

# 명령 하나씩 뽑아와서 실행
for command in command_list:
    # 델타 탐색 / 동, 서, 북, 남
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 명령에 따라 주사위 굴렸을 때 상태 변화
    dice_change = {
        1 : [up, down, bottom, top, left, right],
        2 : [up, down, top, bottom, right, left],
        3 : [top, bottom, left, right, down, up],
        4 : [bottom, top, left, right, up, down],
    }
    # 인덱스 범위를 만족하면
    if 0 <= x + dx[command-1] < N and 0 <= y + dy[command-1] < M:
        # 좌표 이동 / 인덱스라서 -1
        x += dx[command-1]
        y += dy[command-1]
        # 해당 방향으로 주사위 굴리기
        up, down, left, right, top, bottom = dice_change[command]
        # 주사위 윗면 출력 / 인덱스라서 -1
        print(dice[top-1])
        # 지도 해당칸 숫자가 0 이면
        if arr[x][y] == 0:
            # 지도에 주사위 숫자 복사 / 인덱스라서 -1
            arr[x][y] = dice[bottom-1]
        # 지도 해당칸 숫자가 0이 아니면
        else:
            # 주사위 바닥에 지도 해당칸 숫자 복사
            dice[bottom-1] = arr[x][y]
            # 지도 해당칸 숫자 0으로
            arr[x][y] = 0