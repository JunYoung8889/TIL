# 1546_평균 풀이
# 2022-05-05

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N = int(input())
arr = list(map(int, input().split()))
# 최대값 구하기
max_num = max(arr)
# 규칙에 맞춰 점수 조작
for n in range(N):
    arr[n] = arr[n]/max_num*100
# 평균 구하기
ans = sum(arr)/N
print(ans)