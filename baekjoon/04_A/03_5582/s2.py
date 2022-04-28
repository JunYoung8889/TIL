# 5582_공통-부분-문자열 풀이 2
# 2022-04-28
# python3 : 시간초과 / pypy3 : 시간초과

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력 받기
str1 = input()
N = len(str1)
str2 = input()
M = len(str2)

max_ans = 0
for i in range(N):
    # 가지 치기
    if i >= N-max_ans:
        break
    for j in range(M):
        # 같은 문자를 찾으면
        if str1[i] == str2[j]:
            ans = 0
            k = 0
            # 패턴 비교
            while True:
                if i+k >= N or j+k >= M:
                    break
                if str1[i+k] == str2[j+k]:
                    ans += 1
                    k += 1
                else:
                    break
            # 일치한 패턴길이 최장길이 갱신
            if ans > max_ans:
                max_ans = ans
print(max_ans)