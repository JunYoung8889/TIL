# 5670_휴대폰-자판 풀이
# 2022-05-10
# python3 : 시간초과 / pypy3 : 2116ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 트라이 만들기
def make_trie(arr):
    global trie
    for word in arr:
        node = trie
        for char in word:
            if node.get(char) == None:
                node[char] = dict()
            node = node[char]
        node['END'] = 'END'
    return


# 계산 하기
def my_sum(trie):
    global arr, sum
    for word in arr:
        sum += 1
        node = trie
        for char in word[:-1]:
            if len(node[char]) != 1:
                sum += 1
            node = node[char]
    return


# while try except
while True:
    try:
        N = int(input())
        arr = [input() for _ in range(N)]
        trie = dict()
        make_trie(arr)
        sum = 0
        my_sum(trie)
        print('%0.2f'%(sum/N))
    except:
        break