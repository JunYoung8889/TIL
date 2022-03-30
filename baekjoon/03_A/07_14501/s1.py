# 14501_퇴사 풀이
# 2022-03-30

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 상담 함수 구현하기
# day : 날짜 / now_sum : 현재 이익 합계
def consulting(day, now_sum):
    global N, arr, max_sum
    # 퇴사 날짜 초과
    if day > N+1:
        # 탐색 종료
        return
    # 퇴사 날짜 달성
    if day == N+1:
        # 현재 이익이 최대 이익 보다 크면
        if now_sum > max_sum:
            # 최대 이익 갱신
            max_sum = now_sum
        # 탐색 종료
        return
    # 아직 퇴사 날짜가 안됐으면
    else:
        # 상담 하기 / idx 라서 day-1
        consulting(day + arr[day-1][0], now_sum + arr[day-1][1])
        # 상담 안하고 건너 뛰기
        consulting(day + 1, now_sum)
        # 탐색 종료
        return


# 날짜 입력 받기 / N+1일 퇴사
N = int(input())
# 상담 자료 배열 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
consulting(1,0)
print(max_sum)