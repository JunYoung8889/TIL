import sys
sys.stdin = open('input.txt','r')


# len() 구현
def my_len(para_list):
    cnt = 0
    for i in para_list:
        cnt += 1
    return cnt


# 색칠된 공간 표기할 리스트 초기화
box_list = []

# 입력 4줄 받는걸로 정해져있음
for i in range(4):

    # (x1,y1), (x2,y2) 좌표 입력받기
    x1, y1, x2, y2 = map(int,input().split())

    # 색칠 영역 전체 리스트에 추가해주기
    # (x2,y2)는 우상단 좌표이므로
    # (x1,y1)과 같은 조건으로 좌하단으로 해당영역을 표시하면 (x2-1,y2-1)
    for j in range(x1,x2):
        for k in range(y1,y2):

            # 이미 색칠된 영역이 아니라면
            if (j,k) not in box_list:

                # 전체 리스트에 해당 영역을 색칠해라
                box_list.append((j,k))

# 색칠된 총 영역의 개수 출력
print(my_len(box_list))