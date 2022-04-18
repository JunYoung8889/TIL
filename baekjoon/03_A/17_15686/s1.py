# 15686_치킨-배달 풀이
# 2022-04-18

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 집, 치킨집 위치 찾기
def find_home_chicken():
    global N, arr, chicken_list, home_list
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                chicken_list.append((i, j))
            if arr[i][j] == 1:
                home_list.append((i, j))
    return


# nCr 구현하기 n : chicken_cnt, r : M
def comb(picked, cnt):
    global M, chicken_list, chicken_cnt, comb_list
    if cnt == M:
        chicken = []
        for idx in picked:
            chicken.append(chicken_list[idx])
        comb_list.append(chicken)
        return
    else:
        for i in range(chicken_cnt):
            if cnt == 0:
                comb(picked[:] + [i], cnt + 1)
            else:
                if i > picked[-1]:
                    comb(picked[:] + [i], cnt + 1)
        return


# 최소 값 찾기
def find_min_ans():
    global comb_list, home_list, min_ans, N
    for chicken in comb_list:
        ans = 0
        for hi, hj in home_list:
            distance_list = []
            for ci, cj in chicken:
                distance_list.append(abs(hi-ci)+abs(hj-cj))
            ans += min(distance_list)
            if ans >= min_ans:
                break
        if ans < min_ans:
            min_ans = ans


# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨집 위치 리스트 구하기
chicken_list = []
home_list = []
find_home_chicken()
chicken_cnt = len(chicken_list)
home_cnt = len(home_list)

# nCr 구하기
comb_list = []
comb([], 0)

# 최소값 구하기
min_ans = 1e9
find_min_ans()
print(min_ans)