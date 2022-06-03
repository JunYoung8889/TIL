# 1697_숨바꼭질 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 재귀로 하면 에러가 뜸
# bfs로 구현하자!
def find_sister_bfs():
    global N, K, min_ans
    # 넉넉하게 30만 사이즈
    visited = [0] * int(3e5)
    queue = [N]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        now = queue[front]
        # 후진, 전진, 순간이동
        for new in [now -1, now + 1, now * 2]:
            # 인덱스 범위 확인
            if new < 0 or new > 2 * K:
                continue
            # 방문 확인
            if visited[new] != 0:
                continue
            queue.append(new)
            visited[new] = visited[now] + 1
            rear += 1
            # 발견
            if new == K:
                min_ans = visited[new]
                return


# 입력 받기
N, K = map(int, input().split())

# 후진만 가능한 경우
if K <= N:
    print(N - K)

# 전진, 후진, 순간이동 가능한 경우
else:
    min_ans = K - N
    find_sister_bfs()
    print(min_ans)