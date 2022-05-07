# 1085_직사각형에서-탈출 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

x, y, w, h = map(int, input().split())

ans = min([x, y, w-x, h-y])
print(ans)