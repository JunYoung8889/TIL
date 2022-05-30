# 1260_DFS와_BFS 풀이
# 2022-03-09

# 입력파일 받아오기
import sys
sys.stdin = open('input.txt', 'r')

# N : 노드 개수
# M : 간선 개수
# V : 출발 노드
N, M, V = map(int, input().split())

# arr : 간선 배열 입력 받기
# narr : 양방향 인거 고려해서 다시 배열 재배치 및 정렬
arr = [list(map(int, input().split())) for _ in range(M)]
narr = arr + [ [_[1],_[0]] for _ in arr ]
narr.sort()

# dfs 는 재귀적으로 풀기 위해 global 변수로 dfs_list를 밖에서 초기화
dfs_list = []


# DFS 구현
def dfs(para_arr, para_V):
    global dfs_list
    # 출발지점 추가
    dfs_list.append(para_V)
    # 간선 하나씩 검사
    for line in para_arr:
        # 해당 간선의 출발지가 출발 노드와 같고,
        # 해당 간선의 도착지가 방문한적 없으면
        if line[0] == para_V and line[1] not in dfs_list:
            # 해당 간선의 도착지를 출발지로 재귀함수 호출
            dfs(para_arr, line[1])
    # dfs_list 변수를 global로 선언 후 작업을 해서 리턴 받을게 없음
    return None


# BFS 구현
def bfs(para_arr, para_V):
    # BFS는 큐를 쓰자!
    queue = [para_V]
    bfs_list = []
    # 큐가 빌 때까지 반복 작업하자!
    while queue:
        # 큐의 앞 대가리를 빼와서 출발!
        start = queue.pop(0)
        bfs_list.append(start)
        # 간선 하나씩 검사
        for line in para_arr:
            # 해당 간선의 출발지가 출발 노드와 같고,
            # 해당 간선의 도착지가 방문한적 없고,
            # 해당 간선의 도착지가 큐에 이미 대기중이 아니면,
            if line[0] == start and line[1] not in bfs_list and line[1] not in queue:
                # 해당 간선의 도착지를 큐의 출발 대기목록에 추가
                queue.append(line[1])
    # bfs_list를 리턴받는다.
    return bfs_list


dfs(narr,V)
print(*dfs_list)
print(*bfs(narr, V))