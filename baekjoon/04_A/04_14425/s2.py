# 14425_문자열-집합 풀이
# 2022-05-03
# python3 : 6884ms / pypy3 : 4808ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N, M = map(int, input().split())
N_list = [input() for _ in range(N)]
M_list = [input() for _ in range(M)]
# 트라이 구조 연습
trie = dict()
# 트라이 생성
for N_word in N_list:
    node = trie
    for N_char in N_word:
        if node.get(N_char) == None:
            node[N_char] = dict()
            node = node[N_char]
        else:
            node = node[N_char]
    node['END'] = 'END'
# cnt 초기화
cnt = 0
# 트라이 탐색
for M_word in M_list:
    node = trie
    for M_char in M_word:
        if node.get(M_char) == None:
            break
        node = node[M_char]
    else:
        if node.get('END') != None:
            cnt += 1
print(cnt)