# 2559_수열 풀이
# 2022-02-22

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N : 원소 개수
# K : 구간 원소 개수
# arr : 배열
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# small : 구간합
small = 0
# 구간합 초기화
for i in range(K):
    small += arr[i]

# ans : 최대값
ans = small
for i in range(K,N):
    # 구간합 갱신
    small += arr[i] - arr[i-K]
    # 최대값 갱신
    if small > ans:
        ans = small
print(ans)