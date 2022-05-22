# 1043_거짓말 풀이
# 2022-05-22
# python3 : 72ms / pypy3 : 112ms

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


# N : 사람 수 / M : 파티 수
# arr : 진실 리스트 / parent : 부모 리스트
# party_list : 파티 리스트
N, M = map(int, input().split())
arr = list(map(int, input().split()))
parent = list(range(N + 1))
party_list = [list(map(int, input().split())) for _ in range(M)]
# Union_parent 작업
for party in party_list:
    for i in range(1, party[0]):
        a = party[i]
        b = party[i+1]
        union_parent(parent, a, b)

# arr_parent : 진실 부모 리스트
arr_parent = []
for i in arr[1:]:
    arr_parent.append(find_parent(parent, i))

# 거짓말 할 수 있는 파티 카운트
cnt = 0
for party in party_list:
    for i in range(1, party[0] + 1):
        a = party[i]
        # 진실 지인이 해당 파티에 한명이라도 있으면
        if find_parent(parent, a) in arr_parent:
            break
    # 거짓말 가능
    else:
        cnt += 1
print(cnt)