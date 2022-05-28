# 1141_합-구하기 풀이
# 2022-05-29

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N : 원소 개수, arr : 숫자 배열, M : 케이스 개수
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# sum_list : 누적합 리스트
sum_list = [0]
total = 0
for n in arr:
    total += n
    sum_list.append(total)

# 각 케이스 별 구간합 계산 / sum_list[R] - sum_list[L-1]
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])