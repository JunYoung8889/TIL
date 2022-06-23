# 2252_줄-세우기 풀이
# 2022-06-23
# pypy3 : 284ms / python3 : 4212ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# queue로 구현!
def find_ans():
    global N, M, child_num, child_list, parent_list, result
    # 초기화 작업
    queue = []
    front = -1
    rear = -1
    for i in range(N):
        if child_num[i] == 0:
            queue.append(i + 1)
            rear += 1

    # 큐가 빌 때까지 탐색
    while front != rear:
        front += 1
        now = queue[front]
        result.append(now)
        for parent in parent_list[now - 1]:
            child_num[parent - 1] -= 1
            if child_num[parent - 1] == 0:
                queue.append(parent)
                rear += 1
    return


# 입력받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# child_num : 자식 수
# child_list : 자식 리스트
# parent_list : 부모 리스트
child_num = [0] * N
child_list = [[] for _ in range(N)]
parent_list = [[] for _ in range(N)]
for child, parent in arr:
    child_num[parent-1] += 1
    child_list[parent-1].append(child)
    parent_list[child-1].append(parent)

# 결과를 반환받을 변수 초기화
result = []
# 탐색 및 출력
find_ans()
print(*result)