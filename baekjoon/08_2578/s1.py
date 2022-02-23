# 2578_빙고 풀이
# 2022-02-23

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# my_arr : 내 빙고판
my_arr = [list(map(int, input().split())) for _ in range(5)]

# binggo_arr : 사회자 빙고판
binggo_arr = []
for i in range(5):
    binggo_arr.extend(map(int, input().split()))

# cnt : 사회자가 부른 숫자 개수
cnt = 0
for num in binggo_arr:
    cnt += 1

    # 숫자 체크
    for j in range(5):
        for k in range(5):
            if my_arr[j][k] == num:
                my_arr[j][k] = 0

    # 빙고 체크
    binggo_cnt = 0

    # 가로줄 체크
    for j in range(5):
        small_sum = 0
        for k in range(5):
            small_sum += my_arr[j][k]
        if small_sum == 0:
            binggo_cnt += 1

    # 세로줄 체크
    for j in range(5):
        small_sum = 0
        for k in range(5):
            small_sum += my_arr[k][j]
        if small_sum == 0:
            binggo_cnt += 1

    # 대각선1 체크
    small_sum = 0
    for j in range(5):
        small_sum += my_arr[j][j]
    if small_sum == 0:
        binggo_cnt += 1

    # 대각선2 체크
    small_sum = 0
    for j in range(5):
        small_sum += my_arr[j][4-j]
    if small_sum == 0:
        binggo_cnt += 1

    # 빙고 3줄 이상 체크
    if binggo_cnt >= 3:
        break
print(cnt)