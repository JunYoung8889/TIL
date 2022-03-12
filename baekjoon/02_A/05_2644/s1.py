# 2644_촌수계산 풀이
# 2022-03-12

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 최단거리 문제는 bfs로 풀면 쉽다!
def bfs(para_arr, para_start, para_end):
    # bfs는 queue로 풀면 좋다!
    queue = [para_start]
    # visited : 방문한 리스트
    visited = []
    # ans : para_start와 촌수 관계 딕셔너리 자신은 0촌
    ans = {para_start:0}
    # queue가 빌 때까지 해보자!
    while queue:
        # 큐는 앞에서 부터 빼온다.
        start = queue.pop(0)
        visited.append(start)
        # 배열에서 간선을 하나씩 뽑아와서 살펴보자!
        for line in para_arr:
            # 간선의 출발지가 해당 출발지와 같으면
            if line[0] == start:
                # 간선의 도착지가 방문한적 없으면
                if line[1] not in visited:
                    # 큐에 해당 도착지들을 출발 대기열에 추가
                    queue.append(line[1])
                    # ans 에 촌수 관계 추가
                    ans[line[1]] = ans[line[0]] + 1
    # 촌수 관계가 없으면
    if ans.get(para_end) == None:
        # -1 반환
        return -1
    # 촌수 관계가 있으면
    else:
        # 촌수 반환
        return ans.get(para_end)


# N : 사람 수
N = int(input())
# start, end 촌수를 계산해야 하는 서로 다른 두 사람의 번호
start, end = map(int, input().split())
# M : 간선의 수
M = int(input())
# arr : 간선의 배열
arr = [list(map(int, input().split())) for _ in range(M)]
# narr : 양방향 이동이 가능한점 고려해서 배열 추가
narr = arr + [[line[1],line[0]] for line in arr]
print(bfs(narr, start, end))