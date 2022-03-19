# 9205_맥주 마시면서 걸어가기 풀이
# 2022-03-19

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 도착할 수 있는가? 연결되어 있는가?
# 네트워크 문제는 dfs로 풀어보자!
def dfs(arr):
    # 출발지와 목적지
    start = arr[0]
    end = arr[-1]
    # visited : 방문 리스트
    visited = [start]
    # dfs는 stack으로 구현하자
    stack = [start]
    top = 0
    # stack이 빌 때까지 진행하자
    while stack:
        oi, oj = stack[top]
        # 만약에 목적지에 도착 했으면
        if [oi,oj] == end:
            return 'happy'
        # 탐색
        for ni, nj in arr:
            # 방문한적 없으면
            if [ni,nj] not in visited:
                # 거리 = x축 차이 + y축 차이 / 대각선 이동 불가
                distance = abs(ni - oi) + abs(nj - oj)
                # 20병 * 50 = 1000미터 이동가능
                if distance <= 1000:
                    # 방문
                    visited.append([ni,nj])
                    stack.append([ni,nj])
                    top += 1
                    break
        # 방문가능한 곳이 없으면 갈림길로 돌아가자
        else:
            stack.pop()
            top -= 1
    # 전체 탐색 결과 목적지와 연결되어있지 않으면
    return 'sad'


# 테스트 케이스 입력받기
T = int(input())
for t in range(1, T+1):
    # N : 편의점 개수
    N = int(input())
    # arr : 출발지, 편의점, 목적지 좌표 / N+2개
    arr = [list(map(int, input().split())) for _ in range(N+2)]
    ans = dfs(arr)
    print(ans)