# 2527_직사각형 풀이
# 2022-02-26

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 4개 고정
T = 4
for t in range(1, T+1):
    # 사각형 두개 좌표 받기
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # 1번 2번이 좌우 또는 우좌로 겹치지 않는경우
    if p1 < x2 or p2 < x1:
        print('d')
    # 1번 2번이 상하 또는 하상으로 겹치지 않는경우
    elif y1 > q2 or y2 > q1:
        print('d')
    
    # 1번 2번이 밑변 윗변 또는 윗변 밑변으로 겹치는 경우
    elif y1 == q2 or y2 == q1:
        # 1번 2번이 우변 좌변 또는 좌변 우변으로 겹치는 경우
        if x2 == p1 or x1 == p2:
            print('c')
        else:
            print('b')
    
    # 1번 2번이 우변 좌변 또는 좌변 우변으로 겹치는 경우
    elif x2 == p1 or x1 == p2:
        # 1번 2번이 밑변 윗변 또는 윗변 밑변으로 겹치는 경우
        if y1 == q2 or y2 == q1:
            print('c')
        else:
            print('b')

    # 그밖의 경우
    else:
        print('a')