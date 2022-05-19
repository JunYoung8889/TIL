# 2293_동전-1 풀이
# 2022-05-15

import sys
sys.stdin = open('input.txt', 'r')


def find_new(now_num, now_n):
    global n, k, arr, new_cnt
    if now_n == n-2:
        if now_num % arr[now_n] == 0:
            new_cnt += 1
        return
    if now_num//arr[now_n] == 0:
        find_new(now_num, now_n + 1)
    else:
        for i in range(now_num//arr[now_n] + 1):
            find_new(now_num - i * arr[now_n], now_n + 1)


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, k+1):
    new_cnt = 0
    find_new(i, 0)
    dp[i] = dp[i-1] + new_cnt
print(dp[k])