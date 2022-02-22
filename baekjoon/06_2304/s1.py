# 2304_창고_다각형 풀이
# 2022-02-22

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N : 개수
# arr : 배열
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

# 버블소트 정렬
for i in range(N):
    for j in range(N-i-1):
        if arr[j][0] > arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# max 값, 인덱스
max_val = 0
max_idx = 0
for i in range(N):
    if arr[i][1] > max_val:
        max_val = arr[i][1]
        max_idx = i

# 가운데 최대값 으로 초기화
ans = max_val

# 최대값 좌측 영역 구하기
h = 0
for i in range(max_idx):
    if arr[i][1] > h:
        h = arr[i][1]
    ans += (arr[i+1][0] - arr[i][0]) * h

# 최대값 우측 영역 구하기
h = 0
for i in range(N-1,max_idx,-1):
    if arr[i][1] > h:
        h = arr[i][1]
    ans += (arr[i][0] - arr[i-1][0]) * h
print(ans)