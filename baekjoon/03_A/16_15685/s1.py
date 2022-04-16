# 15685_드래곤-커브 풀이
# 2022-04-17

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

'''
a,b를 기준으로 x(y=b)축 대칭 후 y=x(y-b=x-a)축 대칭
x1, y1 = x, 2*b - y
x2, y2 = y1 + a - b, x1 - a + b
'''


# 드래곤 커브 구하기
def dragon_curv():
    global curv_list, cnt
    a, b = curv_list[cnt-1]
    # 기준점을 기준으로 가까운 점 즉, 역순으로 구하자!
    for i in range(cnt-2, -1, -1):
        px, py = curv_list[i]
        curv_list.append((2*b-py+a-b, px-a+b))
    return


# 커브 개수
N = int(input())
# 커브 상태 배열
arr = [list(map(int, input().split())) for _ in range(N)]
# 방향 우, 상, 좌, 하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
# N개의 드래곤 커브의 좌표 리스트를 만들자
dragon = []
# x,y 출발점, d 출발 방향, G 세대
for x, y, d, G in arr:
    curv_list = [(x, y), (x+dj[d], y+di[d])]
    # 세대만큼 커브 증식
    for g in range(G):
        cnt = len(curv_list)
        dragon_curv()
    dragon.append(curv_list)
# 사각형 좌표 받기
dragon_rect = []
for curv in dragon:
    for px, py in curv:
        if 0 <= px <= 100 and 0 <= py <= 100:
            if (px, py) not in dragon_rect:
                dragon_rect.append((px, py))
# 사각형 만들 수 있는 개수 세기
rect_cnt = 0
for px, py in dragon_rect:
    if (px+1,py) in dragon_rect:
        if (px, py+1) in dragon_rect:
            if (px+1, py+1) in dragon_rect:
                rect_cnt += 1
print(rect_cnt)