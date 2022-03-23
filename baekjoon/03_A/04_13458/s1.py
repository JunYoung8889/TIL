# 13458_시험-감독 풀이
# 2022-03-23

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N : 시험장 수
N = int(input())
# arr : 시험장별 응시자 수 배열
arr = list(map(int, input().split()))
# B : 총감독관 1명이 확인가능한 응시생 수
# C : 부감독관 1명이 확인가능한 응시생 수
B, C = map(int, input().split())
# ans = 감독관 수 / 총감독관은 시험장별로 1명씩 배치
ans = N
for i in range(N):
    # 총감독관 혼자 커버 가능하면
    if arr[i] - B <= 0:
        arr[i] = 0
    # 부감독관이 필요하면
    else:
        # 총감독관이 확인한 인원 수
        arr[i] = arr[i] - B
        # 남은 인원이 부감독관이 확인가능한 수로 나누어 떨어지지 않으면
        if arr[i]%C != 0:
            # 몫 + 1
            ans += arr[i]//C + 1
        # 나누어 떨어지면
        else:
            # 몫
            ans += arr[i]//C
print(ans)