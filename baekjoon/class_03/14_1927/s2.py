# 1927_최소-힙 풀이
# 2022-06-05


# heapq 라이브러리 활용
import heapq

# 파일 불러오기
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt' , 'r')

# 입력 받기
N = int(input())
heap = []

# 규칙에 맞춰 출력하기
for _ in range(N):
    num = int(input())
    if num == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)