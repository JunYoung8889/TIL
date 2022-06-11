# 2230_수-고르기 풀이
# 2022-06-11
# python3 : 4792ms, 208ms / 224ms, 164ms


# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 입력받기 / 정렬하기
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 탐색전 초기화 / 1e9하면 15% 에서 틀림
min_ans = int(1e10)
i = 0
j = 1

# 탐색
while True:
    # 같거나 인덱스 범위 넘어가면 처리해주기
    if i == j:
        j += 1
    if j == N:
        break
    if i == N-1:
        break
    
    # 차이 계산
    ans = arr[j] - arr[i]
    
    # 목표에 정확히 일치하면 종료
    if ans == M:
        min_ans = M
        break

    # 목표 보다 크면 왼쪽 증가
    if ans > M:
        i += 1
        if ans < min_ans:
            min_ans = ans

    # 목표 보다 작으면 오른쪽 증가
    elif ans < M:
        j += 1

# 정답 출력
print(min_ans)