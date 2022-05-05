# 14725_개미굴 풀이
# 2022-05-05
# python3 : 112ms / pypy3 : 148ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N = int(input())

# 사전 순서 출력? sort() 개꿀
# [1:]로 받아서 앞에 숫자 빼고 문자열만 받아서 sort()
arr = [input().split()[1:] for _ in range(N)]
arr.sort()

# trie 만들면서 동시에 출력
trie = dict()
for n in range(N):
    path = arr[n]
    node = trie
    k = 0
    for p in path:
        if node.get(p) == None:
            print('--'*k + p)
            node[p] = dict()
        node = node[p]
        k += 1
    node['END'] = 'END'