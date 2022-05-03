# 14425_문자열-집합 풀이
# 2022-05-03
# python3 : 4480ms / pypy3 : 시간초과

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N, M = map(int, input().split())
N_list = [input() for _ in range(N)]
M_list = [input() for _ in range(M)]
# 초기화
cnt = 0
# 한단어씩 뽑아와서
for M_word in M_list:
    # 해당 문자가 N_list에 있는지 체크
    if M_word in N_list:
        cnt += 1
print(cnt)