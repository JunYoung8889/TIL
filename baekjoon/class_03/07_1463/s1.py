# 1463_1로-만들기 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 재귀, 백트레킹
def find_one(now, ans):
    global min_ans, N
    # 탐색 완료
    if now == 1:
        # 갱신
        if ans < min_ans:
            min_ans = ans
        return
    # 가지 치기
    if ans >= min_ans:
        return
    # 탐색
    if now % 3 == 0:
        find_one(now // 3, ans + 1)
    if now % 2 == 0:
        find_one(now // 2, ans + 1)
    find_one(now - 1, ans + 1)
    return


# 입력 받기
N = int(input())
# 초기화
min_ans = int(1e7)
# 탐색
find_one(N, 0)
# 결과 출력
print(min_ans)