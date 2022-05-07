# 1259_팰린드롬수 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

arr = []
while True:
    num = input()
    if num == '0':
        break
    arr.append(num)

for num in arr:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')