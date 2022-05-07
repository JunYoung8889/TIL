# 1181_단어-정렬 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [input() for _ in range(N)]
arr.sort()
ans_list = [[] for _ in range(51)]
for word in arr:
    if word not in ans_list[len(word)]:
        ans_list[len(word)].append(word)

for word_list in ans_list:
    for word in word_list:
        print(word)