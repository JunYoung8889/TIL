# 2675_문자열-반복 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    R, word = input().split()
    R = int(R)
    ans = ''
    for char in word:
        ans += char * R
    print(ans)