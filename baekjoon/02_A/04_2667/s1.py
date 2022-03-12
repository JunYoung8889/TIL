# 2667_단지번호붙이기 풀이
# 2022-03-12

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# len 구현 해보자!
def my_len(para_list):
    cnt = 0
    for num in para_list:
        cnt += 1
    return cnt


# sort 구현 해보자! (버블소트, 오름차순)
def my_sort(para_list):
    for i in range(my_len(para_list)):
        for j in range(my_len(para_list) - 1 - i):
            if para_list[j] > para_list[j+1]:
                para_list[j], para_list[j+1] = para_list[j+1], para_list[j]
    return para_list


# 네트워크 문제는 완전탐색이므로 dfs bfs 둘다 가능!
def dfs(para_arr, para_N):
    # 반환 받을 결과 리스트 초기화
    ans = []
    for i in range(para_N):
        for j in range(para_N):
            # 1이면 집 O / 0이면 집 X
            if para_arr[i][j] == 1:
                # 집을 발견하면 출발!
                start_i = i
                start_j = j
                # 출발하는 순간 집 1개 카운트
                cnt = 1
                # dfs는 stack으로 해보자!
                stack = [[start_i, start_j]]
                # stack이 빌 때까지 해보자!
                while stack:
                    oi, oj = stack[-1]
                    # 방문한 집은 2로 표기하자!
                    para_arr[oi][oj] = 2
                    # 델타탐색 상, 하, 좌, 우!
                    for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                        # new i, j / old i, j
                        ni = oi + di
                        nj = oj + dj
                        # 탐색한 인덱스가 인덱스 범위를 만족하면
                        if 0 <= ni < para_N and 0 <= nj < para_N:
                            # 탐색한 인덱스에 집이 있으면
                            if para_arr[ni][nj] == 1:
                                # 스텍에 해당 경로 추가하고 카운트 증가
                                stack.append([ni,nj])
                                cnt += 1
                                break
                    # 방문 가능한 연결된 집이 없으면
                    else:
                        # 스텍에 해당 출발지 제거
                        # 즉, 이전 출발지(갈림길)로 되돌아가기
                        stack.pop()
                # 결과 리스트에 해당 집 카운트 추가하기
                ans.append(cnt)
    # 연결된 집 수 리스트 반환받기
    return ans


# arr : N * N 행렬
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# ans : 결과 리스트
ans = dfs(arr,N)
# 오름차순 정렬
ans = my_sort(ans)
# 연결된 단지 수
print(my_len(ans))
# 단지내 집의 수를 오름차순으로 출력
for num in ans:
    print(num)