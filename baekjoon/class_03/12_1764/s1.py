# 1764_듣보잡 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N, M = map(int, input().split())
N_list = [input() for _ in range(N)]
M_list = [input() for _ in range(M)]

# M 딕셔너리 만들기
M_dict = dict()
for m in M_list:
    M_dict[m] = 1

# 공통 찾기
N_M_list = []
for n in N_list:
    if M_dict.get(n) != None:
        N_M_list.append(n)

# 사전순 출력
N_M_list.sort()
cnt = len(N_M_list)
print(cnt)
for i in range(cnt):
    print(N_M_list[i])