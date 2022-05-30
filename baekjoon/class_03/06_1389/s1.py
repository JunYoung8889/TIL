# 1389_케빈-베이컨의-6단계-법칙 풀이
# 2022-05-30

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# bfs 구현하기
def bfs(i, j):
    global ans
    visited = [1] + [0] * N
    queue = [i]
    visited[i] = 1
    front = -1
    rear = 0
    while front != rear:
        front += 1
        start = queue[front]
        if start == j:
            break
        for end in arr[start]:
            if end not in queue and visited[end] == 0:
                queue.append(end)
                visited[end] = visited[start] + 1
                rear += 1
    ans += visited[j] - 1


# N : 사람수 / M : 친구 관계 간선 수
N, M = map(int, input().split())

# 간선 배열 만들기
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

# 케빈 베이컨 수 리스트
ans_list = [0] * (N+1)
ans_list[0] = 999999
for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        if i == j:
            continue
        else:
            bfs(i, j)
    ans_list[i] = ans
print(ans_list.index(min(ans_list)))