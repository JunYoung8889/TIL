# 2468_안전 영역 풀이
# 2022-03-19

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# max 구현하기
def my_max(para_list):
    max_num = para_list[0]
    for num in para_list:
        if num > max_num:
            max_num = num
    return max_num


# min 구현하기
def my_min(para_list):
    min_num = para_list[0]
    for num in para_list:
        if num < min_num:
            min_num = num
    return min_num


# 네트워크 문제 DFS로 풀자!
def dfs(para_arr, para_N):
    # visited : 방문 여부 체크 하는 리스트
    visited = [[0]*para_N for _ in range(para_N)]
    # cnt : 연결된 안잠긴 땅 개수
    cnt = 0
    # N * N 행렬 탐색
    for i in range(para_N):
        for j in range(para_N):
            # 잠기지 않았고, 방문한적 없으면
            if para_arr[i][j] != 0 and visited[i][j] == 0:
                # dfs는 stack 으로 구현하자
                stack = [[i,j]]
                top = 0
                visited[i][j] = 1
                # stack이 빌 때까지 탐색
                while stack:
                    oi, oj = stack[top]
                    # 델타탐색 / 상, 하, 좌, 우
                    for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                        # new i,j / old i,j
                        ni = oi + di
                        nj = oj + dj
                        # 인덱스 범위를 만족하면
                        if 0 <= ni < para_N and 0 <= nj < para_N:
                            # 방문한적 없고, 잠기지 않았으면
                            if visited[ni][nj] == 0 and para_arr[ni][nj] != 0:
                                # 스텍에 추가 후 다음 탐색 진행
                                stack.append([ni,nj])
                                top += 1
                                visited[ni][nj] = 1
                                break
                    # 4방향 모두 탐색 불가능이면
                    else:
                        # 이전 갈림길로 돌아가기
                        stack.pop()
                        top -= 1
                # 탐색 완료할 때마다 연결된 안잠긴 땅 개수 증가
                cnt += 1
    # 연결된 안잠긴 땅 개수 반환
    return cnt


# arr : N * N 행렬 / 높이 분포
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1 ~ 100 높이 범위 / 최소 100 최대 1로 초기화 후 최대 최소값 구하기
min_num = 100
max_num = 1
for i in arr:
    if my_max(i) > max_num:
        max_num = my_max(i)
    if my_min(i) < min_num:
        min_num = my_min(i)

# 최소 1개 이므로 1로 초기화
max_ans = 1
for num in range(min_num, max_num):
    # 최소값에서 최대값까지 1칸씩 잠기게 하면서
    # 연결된 안잠긴 땅 개수 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] - 1 > 0:
                arr[i][j] = arr[i][j] - 1
            else:
                arr[i][j] = 0
    ans = dfs(arr,N)
    if ans > max_ans:
        max_ans = ans
# 최대 개수 출력하기
print(max_ans)