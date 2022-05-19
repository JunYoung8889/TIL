# 1654_랜선-자르기 풀이
# 2022-05-19

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# K : 갖고있는 개수 / N : 만들어야되는 개수
K, N = map(int, input().split())
# arr : 갖고있는 랜선 배열
arr = [int(input()) for _ in range(K)]

# 이분 탐색
max_length = max(arr)
start = 1
end = max_length
while True:
    if start > end:
        print(end)
        break
    middle = (start+end)//2
    cnt = 0
    for num in arr:
        cnt += num//middle
    if cnt >= N:
        start = middle + 1
    else:
        end = middle - 1