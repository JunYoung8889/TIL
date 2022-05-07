# 1259_팰린드롬수 풀이
# 2022-05-07

import sys
sys.stdin = open('input.txt', 'r')

arr = []
while True:
    try:
        num = input()
        arr.append(num)
    except:
        break

arr = arr[:-1]
for num in arr:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')