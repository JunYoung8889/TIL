# 2293_동전-1 풀이
# 2022-05-15

import sys
sys.stdin = open('input.txt', 'r')


def find_cnt(now_num, now_n):
    global n, arr, cnt
    if now_n == n-1:
        if now_num % arr[now_n] == 0:
            cnt += 1
        return
    if now_num//arr[now_n] == 0:
        find_cnt(now_num, now_n + 1)
    else:
        for i in range(now_num//arr[now_n] + 1):
            find_cnt(now_num - i * arr[now_n], now_n + 1)


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
cnt = 0
find_cnt(k, 0)
print(cnt)