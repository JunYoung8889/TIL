# 1927_최소-힙 풀이
# 2022-06-04


# 파일 불러오기
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


# 힙에 요소 추가하기
def heap_push(num):
    global heap_list, node
    if node == 1:
        heap_list[node] = num
        node += 1
    else:
        heap_list[node] = num
        node += 1
        heap_sort()
    return


# 힙에 요소 추가시 정렬 해주기
# 상향식 탐색
def heap_sort():
    global heap_list, node
    now = node - 1
    parent = now // 2
    while parent > 0:
        if heap_list[now] < heap_list[parent]:
            heap_list[now], heap_list[parent] = heap_list[parent], heap_list[now]
            now = parent
            parent = now // 2
        else:
            break
    return


# 힙 요소 제거
def heap_delete():
    global node, heap_list, N
    if node == 1:
        return 0
    ans = heap_list[1]
    node -= 1
    heap_list[1] = heap_list[node]
    heap_list[node] = 0
    now = 1
    heap_delete_sort(now)
    return ans


# 힙 요소 제거시 정렬 해주기
# 하향식 탐색
def heap_delete_sort(now):
    global node, heap_list, N
    while True:
        left = now * 2
        right = now * 2 + 1
        smallest = now
        if left < node and heap_list[left] < heap_list[smallest]:
            smallest = left
        if right < node and heap_list[right] < heap_list[smallest]:
            smallest = right
        if smallest != now:
            heap_list[now], heap_list[smallest] = heap_list[smallest], heap_list[now]
            now = smallest
        else:
            break
    return


# 입력 받기
N = int(input())
heap_list = [0] * (N + 2)
node = 1

# 규칙에 맞춰 출력
for _ in range(N):
    num = int(input())
    if num == 0:
        print(heap_delete())
    else:
        heap_push(num)