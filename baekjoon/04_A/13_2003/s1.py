# 2003_수들의-합-2 풀이
# 2022-06-11
# python3 : 76ms / pypy3 : 112ms


# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 탐색 전 초기화
i = 0
j = 0
now = arr[i]
ans = 0

# 탐색
while True:
    # 발견
    if now == M:
        ans += 1

    # 합이 적으면 오른쪽 범위 증가
    if now <= M:
        j += 1
        if j == N:
            break
        now += arr[j]

    # 합이 크면 왼쪽 범위 증가
    else:
        i += 1
        if i == N:
            break
        now -= arr[i-1]

# 정답 출력
print(ans)