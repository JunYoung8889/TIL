# 1717_집합의-표현 풀이
# 2022-05-22
# python3 : 시간초과 / pypy3 : 4888ms

# 파일 불러오기 및 최대재귀깊이 설정
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)


# 부모 찾기 함수
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


# 부모 합치기 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# N : 노드 개수 / M : 간선 개수 / parent : 부모 리스트
N, M = map(int, input().split())
parent = list(range(N+1))
for _ in range(M):
    operator, a, b = map(int, input().split())
    # 합치기
    if operator == 0:
        union_parent(parent, a, b)
    # 부모가 같은지 확인
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')