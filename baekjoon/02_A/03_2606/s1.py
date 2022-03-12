# 2606_바이러스 풀이
# 2022-03-12

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# len을 구현 해보자!
def my_len(para_list):
    cnt = 0
    for num in para_list:
        cnt += 1
    return cnt


# 네트워크 문제는 완전 탐색이므로 dfs bfs 아무꺼나 가능!
def dfs(para_arr):
    # dfs는 stack을 쓰자!
    stack = [1]
    # 방문한 노드는 ans에 추가 해주자!
    ans = [1]
    # stack이 빌 때까지 해보자!
    while stack:
        # stack 의 top 값에서 출발하자!
        start = stack[-1]
        # 배열에서 간선을 하나씩 뽑아오자!
        for line in para_arr:
            # 간선의 출발지가 현재 원하는 출발지와 같으면
            if line[0] == start:
                # 간선의 도착지가 방문한적 없으면
                if line[1] not in ans:
                    # 방문 및 stack에 추가
                    ans.append(line[1])
                    stack.append(line[1])
                    break
        # 현재 출발점에서 이용 가능한 간선이 없으면
        else:
            # stack에서 현재 출발점 제거
            # 즉, 이전 출발점(갈림길)으로 돌아감
            stack.pop()
    # 출발지 1을 제외한 감염 컴퓨터 수
    return my_len(ans)-1


# N : 컴퓨터 수
# M : 간선 수
# arr : 간선 배열
N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
# narr : 양방향 가능한점 고려해서 배열에 추가
narr = arr + [[line[1],line[0]] for line in arr]
print(dfs(narr))