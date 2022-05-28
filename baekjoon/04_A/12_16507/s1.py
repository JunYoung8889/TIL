# 16507_어두운-건-무서워 풀이
# 2022-05-29

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N : 행, M : 열, Q : 케이스 개수, arr : 사진 밝기 배열
N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 누적합 리스트 만들기
sum_list = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    total = 0
    for j in range(M):
        total += arr[i][j]
        sum_list[i+1][j+1] = total

# 구간합 구하기
for q in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    total = 0
    cnt = 0
    for r in range(r1, r2+1):
        total += sum_list[r][c2] - sum_list[r][c1-1]
        cnt += c2 - c1 + 1
    print(total // cnt)