# 1107_리모컨 풀이
# 2022-05-30

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 목표 채널
target = input()

# 초기 채널과 같으면
if target == '100':
    print(0)
    sys.exit()

# 고장난 버튼 수 
N = int(input())

# 고장난 버튼이 없으면
if N == 0:
    if target == '101':
        print(1)
    elif target == '102':
        print(2)
    elif target == '99':
        print(1)
    else:
        print(len(target))
    sys.exit()

# 모든 버튼이 고장났으면
if N == 10:
    print(abs(int(target) - 100))
    sys.exit()

# 고장난 버튼 배열
arr = input().split()
ans = abs(int(target) - 100)
# 완전탐색
for num in range(1000001):
    for n in str(num):
        if n in arr:
            break
    else:
        ans = min(ans, len(str(num)) + abs(int(target) - num))
print(ans)
