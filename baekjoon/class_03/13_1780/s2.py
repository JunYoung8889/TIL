# 1780_종이의-개수 풀이
# 2022-06-04

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 재귀, 분할 정복
def my_count(i, j, n):
    global arr, num_dict
    # 출발 좌표, 값 초기화
    oi = i
    oj = j
    start = arr[oi][oj]
    # 탐색 시작
    for di in range(n):
        for dj in range(n):
            # 모두 같은 수가 아니면!
            if arr[oi + di][oj + dj] != start:
                # 9조각 분할
                for ni in range(3):
                    for nj in range(3):
                        my_count(oi + (n // 3) * ni, oj + (n //3) * nj, n // 3)
                break
        if arr[oi + di][oj + dj] != start:
            break
    # 모두 같으면
    else:
        num_dict[start] += 1
    return


# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 숫자 카운트할 딕셔너리 초기화
num_dict = dict()
num_dict[-1] = 0
num_dict[0] = 0
num_dict[1] = 0

# 탐색
my_count(0, 0, N)

# 결과 출력
for i in num_dict:
    print(num_dict[i])