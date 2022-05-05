# 1330_두-수-비교하기 풀이
# 2022-05-05

import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')