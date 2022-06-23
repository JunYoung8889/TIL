# 2056_작업 풀이2
# 2022-06-23
# python3 : 1460ms / pypy3 : 308ms


# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# queue로 구현!
def find_ans():
    global N, arr, child_num, child_list, result, parent_list

    # 초기화
    queue = []
    front = -1
    rear = -1
    for i in range(N):
        if child_num[i] == 0:
            queue.append(i+1)
            rear += 1

    # queue가 빌 때까지 탐색
    while front != rear:
        front += 1
        now = queue[front]
        for parent in parent_list[now-1]:
            # 간선제거
            child_num[parent - 1] -= 1
            # 다음 노드 추가
            if child_num[parent - 1] == 0:
                queue.append(parent)
                rear += 1
            # 갱신
            result[parent-1] = max(result[parent-1], result[now-1] + arr[parent-1][0])
    return


# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [work[0] for work in arr]

# child_num : 들어오는 간선 수
# child_list : 들어오는 노드 번호들
# parent_list : 부모 리스트
child_num = [0] * N
child_list = [[] for _ in range(N)]
parent_list = [[] for _ in range(N)]
for i in range(N):
    child_num[i] = arr[i][1]
    child_list[i] = arr[i][2:]
    for child in child_list[i]:
        parent_list[child - 1].append(i+1)

find_ans()
print(max(result))