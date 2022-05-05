# 2577_숫자의-개수 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

A, B, C = [int(input()) for _ in range(3)]
int_num = A * B * C
str_num = str(int_num)
count_list = [0]*10
for num in str_num:
    count_list[int(num)] += 1
for ans in count_list:
    print(ans)