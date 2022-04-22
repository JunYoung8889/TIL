# 17144_미세먼지-안녕! 풀이
# 2022-04-22
# python3 : 시간초과 / pypy3 : 440ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 먼지 확산
def dirty():
    global R, C, arr
    # 먼지 위치 및 양 체크
    dust_idx_list = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                dust_idx_list.append((i, j, arr[i][j]))

    for oi, oj, dust in dust_idx_list:
        # 확산한 양 카운트
        diffuse_amount = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = oi + di
            nj = oj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] != -1:
                    arr[ni][nj] += int(dust/5)
                    diffuse_amount += int(dust/5)
        # 모든방향 탐색 이후 마지막에 확산한 양 빼주기
        arr[oi][oj] -= diffuse_amount
    return


# 먼지 순환
def clean():
    global R, C, arr, LG_WHISEN_bottom, LG_WHISEN_head
    # 머리부 순환
    hi, hj = LG_WHISEN_head
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    k = 0
    ni, nj = hi-1, hj
    while True:
        oi, oj = ni, nj
        di, dj = delta[k]
        ni += di
        nj += dj
        if (ni, nj) == (hi, hj):
            arr[oi][oj] = 0
            break
        if 0 <= ni < hi+1 and 0 <= nj < C:
            arr[oi][oj] = arr[ni][nj]
        else:
            ni -= di
            nj -= dj
            k += 1
    
    # 바닥부 순환
    bi, bj = LG_WHISEN_bottom
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    k = 0
    ni, nj = bi+1, bj
    while True:
        oi, oj = ni, nj
        di, dj = delta[k]
        ni += di
        nj += dj
        if (ni, nj) == (bi, bj):
            arr[oi][oj] = 0
            break
        if bi <= ni < R and 0 <= nj < C:
            arr[oi][oj] = arr[ni][nj]
        else:
            ni -= di
            nj -= dj
            k += 1
    return


# 1초
def sec():
    dirty()
    clean()
    return


# R행 C열 T초
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
for i in range(2,R-2):
    if arr[i][0] == -1:
        LG_WHISEN_head = (i, 0)
        LG_WHISEN_bottom = (i+1, 0)
        break

# T초 경과
for _ in range(T):
    sec()

# 최종 먼지 양 카운트
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != 0 and arr[i][j] != -1:
            ans += arr[i][j]

print(ans)