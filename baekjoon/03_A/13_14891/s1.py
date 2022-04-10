# 14891_톱니바퀴 풀이
# 2022-04-10

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 1번 톱니 회전
def game1(d):
    global t1, t2, t3, t4
    # 연결 부위 체크
    check2, check3, check4 = False, False, False
    if t1[2] != t2[6]:
        check2 = True
    if t2[2] != t3[6]:
        check3 = True
    if t3[2] != t4[6]:
        check4 = True
    # 1 : cw / 시계 방향
    if d == 1:
        t1 = [t1[7]] + t1[:7]
        # 2, 3, 4 순으로 체크 및 회전
        if check2 == True:
            t2 = t2[1:] + [t2[0]]
            if check3 == True:
                t3 = [t3[7]] + t3[:7]
                if check4 == True:
                    t4 = t4[1:] + [t4[0]]
    # -1 : ccw / 반시계 방향
    else:
        t1 = t1[1:] + [t1[0]]
        if check2 == True:
            t2 = [t2[7]] + t2[:7]
            if check3 == True:
                t3 = t3[1:] + [t3[0]]
                if check4 == True:
                    t4 = [t4[7]] + t4[:7]


# 2번 톱니 회전
def game2(d):
    global t1, t2, t3, t4
    # 연결 부위 체크
    check1, check3, check4 = False, False, False
    if t1[2] != t2[6]:
        check1 = True
    if t2[2] != t3[6]:
        check3 = True
    if t3[2] != t4[6]:
        check4 = True
    # 1 : cw / 시계 방향
    if d == 1:
        t2 = [t2[7]] + t2[:7]
        # 1 체크 및 회전
        if check1 == True:
            t1 = t1[1:] + [t1[0]]
        # 3, 4 순으로 체크 및 회전
        if check3 == True:
            t3 = t3[1:] + [t3[0]]
            if check4 == True:
                t4 = [t4[7]] + t4[:7]
    # -1 : ccw / 반시계 방향
    else:
        t2 = t2[1:] + [t2[0]]
        if check1 == True:
            t1 = [t1[7]] + t1[:7]
        if check3 == True:
            t3 = [t3[7]] + t3[:7]
            if check4 == True:
                t4 = t4[1:] + [t4[0]]


# 3번 톱니 회전
def game3(d):
    global t1, t2, t3, t4
    # 연결 부위 체크
    check1, check2, check4 = False, False, False
    if t1[2] != t2[6]:
        check1 = True
    if t2[2] != t3[6]:
        check2 = True
    if t3[2] != t4[6]:
        check4 = True
    # 1 : cw / 시계 방향
    if d == 1:
        t3 = [t3[7]] + t3[:7]
        # 4 체크 및 회전
        if check4 == True:
            t4 = t4[1:] + [t4[0]]
        # 2, 1 순으로 체크 및 회전
        if check2 == True:
            t2 = t2[1:] + [t2[0]]
            if check1 == True:
                t1 = [t1[7]] + t1[:7]
    # -1 : ccw / 반시계 방향
    else:
        t3 = t3[1:] + [t3[0]]
        if check4 == True:
            t4 = [t4[7]] + t4[:7]
        if check2 == True:
            t2 = [t2[7]] + t2[:7]
            if check1 == True:
                t1 = t1[1:] + [t1[0]]


# 4번 톱니 회전
def game4(d):
    global t1, t2, t3, t4
    # 연결 부위 체크
    check1, check2, check3 = False, False, False
    if t1[2] != t2[6]:
        check1 = True
    if t2[2] != t3[6]:
        check2 = True
    if t3[2] != t4[6]:
        check3 = True
    # 1 : cw / 시계 방향
    if d == 1:
        t4 = [t4[7]] + t4[:7]
        # 3, 2, 1 순으로 체크 및 회전
        if check3 == True:
            t3 = t3[1:] + [t3[0]]
            if check2 == True:
                t2 = [t2[7]] + t2[:7]
                if check1 == True:
                    t1 = t1[1:] + [t1[0]]
    # -1 : ccw / 반시계 방향
    else:
        t4 = t4[1:] + [t4[0]]
        if check3 == True:
            t3 = [t3[7]] + t3[:7]
            if check2 == True:
                t2 = t2[1:] + [t2[0]]
                if check1 == True:
                    t1 = [t1[7]] + t1[:7]


# 0 : N / 1 : S
t1 = list(map(int, input()))
t2 = list(map(int, input()))
t3 = list(map(int, input()))
t4 = list(map(int, input()))
K = int(input())
# cw : 1, ccw: -1
k_arr = [list(map(int, input().split())) for _ in range(K)]
for n, d in k_arr:
    if n == 1:
        game1(d)
    elif n == 2:
        game2(d)
    elif n == 3:
        game3(d)
    elif n == 4:
        game4(d)

score = t1[0] + 2 * t2[0] + 4 * t3[0] + 8 * t4[0]
print(score)