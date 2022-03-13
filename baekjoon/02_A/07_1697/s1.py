# 1697_숨바꼭질 풀이
# 2022-03-13

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 최단거리 문제는 bfs로 해결하자!
def bfs():
    # N : 수빈이 위치 / 출발
    # K : 동생 위치 / 도착
    N, K = map(int, input().split())
    # 같은 위치에 있으면 0초 후에 발견!
    if N == K:
        return 0
    # 동생이 뒤에 있으면
    if N > K:
        # 뒤로는 1칸씩 밖에 이동 못해서 N-K초 후에 발견!
        return N-K
    # bfs는 queue로 해결하자!
    queue = [N]
    # front : 머리 / queue는 머리부터 뽑아온다.
    # rear : 꼬리 / queue는 꼬리에 쌓는다.
    front = -1
    rear = 0
    # time_list : 방문하는데 걸린 시간을 계산한다.
    # 넉넉하게 300,000칸 만들어둔다.
    time_list = [0]*300000
    # front == rear가 되면 queue가 비었다는 뜻!
    while front != rear:
        # queue의 머리에서 뽑아오면 머리는 하나 증가!
        front += 1
        start = queue[front]
        # 이동 방식 3가지 / 후진, 전진, 순간이동
        for new in [start-1, start+1, start*2]:
            # start가 0일 떄, new가 -1이 되는 경우 제외 시키기
            if new == -1:
                continue
            # new가 도착지의 두배를 넘어가는 경우 제외 시키기
            if new > 2*K:
                continue
            # 방문한적 없으면!
            if time_list[new]==0:
                # queue의 꼬리에 추가하고 꼬리는 하나 증가!
                queue.append(new)
                rear += 1
                # 방문하는데 걸린 시간 표시
                time_list[new] = time_list[start] + 1
                # 원하는 목적지에 도착하면
                if new == K:
                    # 도착하는데 걸린시간 반환
                    return time_list[K]


print(bfs())