# 5014_스타트링크 풀이
# 2022-03-13

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 최단거리 문제는 bfs로 해결하자!
def bfs():
    # F : 최고층 / S : 출발층 / G : 도착층
    # U : 위로 U칸 버튼 / D : 아래로 D칸 버튼
    F, S, G, U, D = map(int, input().split())
    # 출발지와 도착지가 같으면
    if S == G:
        # 버튼 누르는 횟수 0회 반환
        return 0
    # cnt_list : 해당층까지 오는데 누른 버튼 횟수 기록
    cnt_list = [0]*(F+1)
    # bfs는 queue로 구현하자!
    queue = [S]
    # front : 머리 / queue는 머리에서 뽑아온다.
    # rear : 꼬리 / queue는 꼬리에 쌓는다.
    front = -1
    rear = 0
    # front == rear 이면 queue가 빈 상태를 의미한다.
    while front != rear:
        # queue에서 뽑아올 때는 머리에서 뽑고 머리를 1증가
        front += 1
        start = queue[front]
        # 위로 U칸 가거나, 아래로 D칸 가거나
        for new in [start+U,start-D]:
            # 1층 에서 F층 까지 이동 가능
            if 1<= new < F+1:
                # 방문한적 없으면
                if cnt_list[new] == 0:
                    # queue에 쌓을 때는 꼬리에 쌓고 꼬리를 1증가
                    queue.append(new)
                    rear += 1
                    # 현재층까지 오는데 누른 버튼 횟수 기록
                    cnt_list[new] = cnt_list[start] + 1
                    # 도착했으면
                    if new == G:
                        # U가 0인 경우
                        # 처음에 무의미하게 U를 누른 것으로 간주해서
                        # 1회 빼준 값이 정답이다.
                        if U == 0:
                            return cnt_list[G] - 1
                        # 나머지 경우에는 해당값이 정답이다.
                        else:
                            return cnt_list[G]
    # 탐색결과 엘리베이터로 이동할 수 없을 때는
    return 'use the stairs'


print(bfs())