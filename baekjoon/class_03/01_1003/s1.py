# 1003_피보나치-함수 풀이
# 2022-05-28

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 피보나치 호출 횟수 함수 구현
def fibonacci(num):
    global cnt0, cnt1
    len_cnt0 = len(cnt0)
    if num >= len_cnt0:
        for i in range(len_cnt0, num+1):
            cnt0.append(cnt0[i-1] + cnt0[i-2])
            cnt1.append(cnt1[i-1] + cnt1[i-2])
    return


# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # target
    N = int(input())
    # cnt0 : 0 호출 횟수 / cnt1 : 1 호출 횟수
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    fibonacci(N)
    print(cnt0[N], cnt1[N])