# 14888_연산자-끼워넣기 풀이
# 2022-04-05

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 재귀 함수로 완탐
def find_min_max(idx, now_sum, plus, minus, mult, div):
    global N, arr, min_ans, max_ans
    # 도착
    if idx == N-1:
        if now_sum < min_ans:
            min_ans = now_sum
        if now_sum > max_ans:
            max_ans = now_sum
        return
    # 진행 중
    else:
        if plus != 0:
            find_min_max(idx + 1, now_sum + arr[idx+1], plus-1, minus, mult, div)
        if minus != 0:
            find_min_max(idx + 1, now_sum - arr[idx+1], plus, minus-1, mult, div)
        if mult != 0:
            find_min_max(idx + 1, now_sum * arr[idx+1], plus, minus, mult-1, div)
        if div != 0:
            if now_sum < 0:
                find_min_max(idx + 1, -(-now_sum//arr[idx+1]), plus, minus, mult, div-1)
            else:
                find_min_max(idx + 1, now_sum//arr[idx+1], plus, minus, mult, div-1)
        return


# N 숫자 개수
# arr : 숫자 배열
N = int(input())
arr = list(map(int, input().split()))
# 연산자 개수
plus, minus, mult, div = map(int, input().split())


# max, min 초기화
max_ans = -1e9
min_ans = 1e9
# 재귀함수 완탐
find_min_max(0, arr[0], plus, minus, mult, div)
print(max_ans)
print(min_ans)