# 2056_작업 풀이
# 2022-06-22
# python3 : 시간초과 / pypy3 : 3008ms


# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# queue로 구현!
def find_ans():
    global N, arr, child_num, child_list, result

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
        for i in range(now, N):
            if now in child_list[i]:
                # 간선제거
                child_num[i] -= 1
                
                # 다음 노드 추가
                if child_num[i] == 0:
                    queue.append(i+1)
                    rear += 1
                
                # 갱신
                result[i] = max(result[i], result[now-1] + arr[i][0])
    return


# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [work[0] for work in arr]

# child_num : 들어오는 간선 수
# child_list : 들어오는 노드 번호들
child_num = [0] * N
child_list = [[] for _ in range(N)]
for i in range(N):
    child_num[i] = arr[i][1]
    child_list[i] = arr[i][2:]

find_ans()
print(max(result))