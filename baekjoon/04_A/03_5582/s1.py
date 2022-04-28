# 5582_공통-부분-문자열 풀이
# 2022-04-28
# python3 : 시간초과, 메모리초과 / pypy3 : 448ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력 받기
str1 = input()
M = len(str1)
str2 = input()
N = len(str2)
# N+1 * M+1 행렬 만들기
arr = [[0]*(M+1)]+[[0]*(M+1) for _ in range(N)]
# 규칙에 맞춰 2차원 배열 값 채워넣기
for i in range(N):
    for j in range(M):
        # 같은 문자면 왼쪽 대각선 위 값 더하기 1
        if str2[i] == str1[j]:
            arr[i+1][j+1] = arr[i][j] + 1
# 최대값 구하기
print(max(map(max, arr)))