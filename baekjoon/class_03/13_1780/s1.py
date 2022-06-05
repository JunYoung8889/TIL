# 1780_종이의-개수 풀이
# 2022-06-04

import sys
sys.stdin = open('input.txt', 'r')


def my_count():
    global N, arr, num_dict
    queue = [(0, 0, 0)]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        if front == 50:
            queue = queue[50:]
            front = 0
            rear -= 50
        oi, oj, cnt = queue[front]
        start = arr[oi][oj]
        for di in range(N // (3 ** cnt)):
            for dj in range(N // (3 ** cnt)):
                if arr[oi + di][oj + dj] != start:
                    cnt += 1
                    for ni in range(3):
                        for nj in range(3):
                            queue.append((oi + (N // (3 ** cnt))*ni, oj + (N // (3 ** cnt))*nj, cnt))
                            rear += 1
                    break
            if arr[oi + di][oj + dj] != start:
                break
        else:
            num_dict[start] += 1


N = int(input())
num_dict = dict()
num_dict[-1] = 0
num_dict[0] = 0
num_dict[1] = 0
arr = [list(map(int, input().split())) for _ in range(N)]
my_count()
for i in num_dict:
    print(num_dict[i])