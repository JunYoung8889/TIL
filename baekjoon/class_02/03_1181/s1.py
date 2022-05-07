# 1181_단어-정렬 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for word in arr:
    print(word)