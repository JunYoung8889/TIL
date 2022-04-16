# 15683_감시 풀이
# 2022-04-16

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# cctv 번호에 따른 탐색 방향
cctv_dict = {
    1 : [[0], [1], [2], [3]],
    2 : [[0, 2], [1, 3], [2, 0], [3, 1]],
    3 : [[0, 1], [1, 2], [2, 3], [3, 0]],
    4 : [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5 : [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0 ,1, 2]],
}
# 델타 상 우 하 좌
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# '#' 마킹 해주는 함수
def check(i, j, num, direction):
    global N, M, arr, cctv_dict, delta
    check_list = []
    oi, oj = i, j
    d_list = cctv_dict[num][direction]
    for d in d_list:
        di, dj = delta[d]
        ni, nj = oi, oj
        while True:
            ni += di
            nj += dj
            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                break
            if arr[ni][nj] == 6:
                break
            if arr[ni][nj] == 0:
                arr[ni][nj] = '#'
                check_list.append((ni, nj))
    return check_list


# '#' 마킹을 해제 해주는 함수
def delete(check_list):
    global arr
    for i, j in check_list:
        arr[i][j] = 0


# 0개수 카운트 함수
def count_safezone():
    global N, M, arr, min_ans
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
                if cnt >= min_ans:
                    return cnt
    return cnt


# 최소값 찾기
def find_min(idx):
    global cctv_list, cctv_cnt, cctv_dict, min_ans
    # 모든 cctv 탐색을 완료 했으면
    if idx == cctv_cnt:
        # 개수 카운트 후 최소값 갱신
        ans = count_safezone()
        if ans < min_ans:
            min_ans = ans
        return
    # 모든 cctv 탐색을 완료하지 못했으면
    else:
        # i,j 좌표, num : cctv 번호
        i, j, num = cctv_list[idx]
        for direction in range(4):
            # cctv 체크
            check_list = check(i, j, num, direction)
            # 다음 cctv 체크
            find_min(idx+1)
            # cctv 체크 해제
            delete(check_list)
        return


# N * M 행렬
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# cctv 위치와 번호를 체크해서 리스트에 담자!
cctv_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv_list.append((i, j, arr[i][j]))
# cctv 개수
cctv_cnt = len(cctv_list)
# 최소값 초기화
min_ans = N * M
# 최소값 찾기
find_min(0)
print(min_ans)