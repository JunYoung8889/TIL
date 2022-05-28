# 1966_프린터-큐 풀이
# 2022-05-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    # N : 문서 개수 / idx : 궁금한 문서 위치
    N, idx = map(int, input().split())
    
    # queue로 풀자!
    queue = list(map(int, input().split()))
    cnt = 1
    while True:
        tmp = queue.pop(0)
        # 마지막 원소
        if queue == []:
            print(cnt)
            break
        
        # 가장 우선 순위가 높으면
        if tmp >= max(queue):
            # 찾던 자료면
            if idx == 0:
                print(cnt)
                break
            # 찾던 자료가 아니면
            else:
                idx -= 1
                cnt += 1
        
        # 우선 순위가 낮으면
        else:
            if idx == 0:
                idx = len(queue)
            else:
                idx -= 1
            queue.append(tmp)