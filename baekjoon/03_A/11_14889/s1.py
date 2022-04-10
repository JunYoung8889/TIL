# 14889_스타트와-링크 풀이
# 2022-04-10

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 조합 nCr / n == N / r == N//2
def comb(picked_nums, cnt):
    global N, nums, arr, min_ans
    # 가지치기
    if min_ans == 0:
        return
    # 다뽑았으면
    if cnt == N//2:
        # 팀 1 / 팀 2 : 팀1 제외하고 남은 인원
        team1 = picked_nums[:]
        team2 = set(nums) - set(picked_nums[:])
        # 팀 1 합계 구하기
        team1_sum = 0
        for i1 in team1:
            for j1 in team1:
                team1_sum += arr[i1][j1]
        # 팀 2 합계 구하기
        ans = -team1_sum
        for i2 in team2:
            for j2 in team2:
                ans += arr[i2][j2]
                # 가지치기
                if ans >= min_ans:
                    return
        # 답 구하기
        ans = abs(ans)
        # 최소 답안 갱신
        if ans < min_ans:
            min_ans = ans
        return
    # 덜 뽑았으면
    else:
        for n in nums:
            if cnt == 0:
                comb(picked_nums[:]+[n], cnt+1)
            else:
                if n > picked_nums[-1]:
                    comb(picked_nums[:]+[n], cnt+1)
        return


# arr : N * N 행렬
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 최소값 초기화
min_ans = 100 * N * N
# 인덱스 0 ~ N-1까지
nums = list(range(N))
comb([],0)
print(min_ans)