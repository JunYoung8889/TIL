# 1874_스택-수열 풀이
# 2022-05-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# arr : 1이상 N이하의 정수 배열
N = int(input())
arr = [int(input()) for _ in range(N)]

# stack으로 풀자!
ans = []
n = 1
stack = []
top = -1
idx = 0
while True:
    # 불가능
    if n > N + 1:
        print('NO')
        break
    
    # 완성
    if idx == N:
        for a in ans:
            print(a)
        break
    
    # stack이 비어있으면
    if top == -1:
        stack.append(n)
        n += 1
        top += 1
        ans.append('+')
    
    # stack이 비어있지 않으면
    else:
        # 발견 o
        if stack[top] == arr[idx]:
            stack.pop()
            top -= 1
            idx += 1
            ans.append('-')
        # 발견 x
        else:
            stack.append(n)
            n += 1
            top += 1
            ans.append('+')