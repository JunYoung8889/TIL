# 14499_주사위-굴리기 풀이
# 2022-03-24

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N * M 행렬
# 초기위치 (x,y)
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
up = 2
down = 5
left = 4
right = 3
top = 1
bottom = 6

# 명령 하나씩 뽑아와서 실행
for command in command_list:
    # 동쪽으로 굴리기
    if command == 1:
        # 인덱스 범위를 만족하면
        if y + 1 < M:
            # 동쪽으로 이동
            y += 1
            # 동쪽으로 굴리기 
            up,down,left,right,top,bottom = up,down,bottom,top,left,right
            # 주사위 윗면 출력 / 인덱스라서 -1
            print(dice[top-1])
            # 지도 해당칸 숫자가 0 이면
            if arr[x][y] == 0:
                # 지도에 주사위 숫자 복사
                arr[x][y] = dice[bottom-1]
            # 지도 해당칸 숫자가 0이 아니면
            else:
                # 주사위 바닥에 지도 해당칸 숫자 복사
                dice[bottom-1] = arr[x][y]
                # 지도 해당칸 숫자 0으로
                arr[x][y] = 0

    # 서쪽으로 굴리기
    elif command == 2:
        if y - 1 >= 0:
            y -= 1
            up,down,left,right,top,bottom = up,down,top,bottom,right,left
            print(dice[top-1])
            if arr[x][y] == 0:
                arr[x][y] = dice[bottom-1]
            else:
                dice[bottom-1] = arr[x][y]
                arr[x][y] = 0
    
    # 북쪽으로 굴리기
    elif command == 3:
        if x - 1 >= 0:
            x -= 1
            up,down,left,right,top,bottom = top,bottom,left,right,down,up
            print(dice[top-1])
            if arr[x][y] == 0:
                arr[x][y] = dice[bottom-1]
            else:
                dice[bottom-1] = arr[x][y]
                arr[x][y] = 0
    
    # 남쪽으로 굴리기
    elif command == 4:
        if x + 1 < N:
            x += 1
            up,down,left,right,top,bottom = bottom,top,left,right,up,down
            print(dice[top-1])
            if arr[x][y] == 0:
                arr[x][y] = dice[bottom-1]
            else:
                dice[bottom-1] = arr[x][y]
                arr[x][y] = 0