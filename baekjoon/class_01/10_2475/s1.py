# 2475_검증수 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))

ans = 0
for num in arr:
    ans += num ** 2
ans = ans % 10
print(ans)