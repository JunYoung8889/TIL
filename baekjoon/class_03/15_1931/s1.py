# 1931_회의실-배정 풀이
# 2022-06-05

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 그리디 문제
# 정렬을 잘해야한다.
# 회의가 끝나는 시간 기준으로 정렬, 같으면 시작 시간 기준
arr.sort(key = lambda x : (x[1], x[0]))

# 탐색
end = arr[0][1]
cnt = 1
for i in range(1, N):
    start = arr[i][0]
    if start >= end:
        cnt += 1
        end = arr[i][1]
print(cnt)