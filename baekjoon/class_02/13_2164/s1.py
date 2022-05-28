# 2164_카드2 풀이
# 2022-05-28

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N장의 카드
N = int(input())

# queue로 풀자!
queue = list(range(N+1))[1:]
front = 0
rear = N-1

# queue가 빌 때까지 진행
while front != rear:
    # 하나 버림
    front += 1
    
    # 하나 제일 아래로
    queue.append(queue[front])
    front += 1
    rear += 1

print(queue[front])