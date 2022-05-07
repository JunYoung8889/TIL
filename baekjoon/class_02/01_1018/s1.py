# 1018_체스판-다시-칠하기 풀이
# 2022-05-07

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 흰색 시작 판 기준으로 몇칸 바꿔야되는지 확인
def find_w(i, j):
    global N, M, arr, w_board, ans
    cnt = 0
    for iw in range(i, i+8):
        for jw in range(j, j+8):
            # 가지치기
            if cnt >= ans:
                return
            else:
                if arr[iw][jw] != w_board[iw-i][jw-j]:
                    cnt += 1
    if cnt < ans:
        ans = cnt


# 검정색 시작 판 기준으로 몇칸 바꿔야되는지 확인
def find_b(i, j):
    global N, M, arr, b_board, ans
    cnt = 0
    for ib in range(i, i+8):
        for jb in range(j, j+8):
            # 가지치기
            if cnt >= ans:
                return
            else:
                if arr[ib][jb] != b_board[ib-i][jb-j]:
                    cnt += 1
    if cnt < ans:
        ans = cnt


# 입력 받기
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# w_board : 8*8 사이즈 흰색 시작 판
# b_board : 8*8 사이즈 검정색 시작 판
w_board = []
b_board = []
for n in range(8):
    if n % 2 == 0:
        w_board.append('WB'*4)
        b_board.append('BW'*4)
    else:
        w_board.append('BW'*4)
        b_board.append('WB'*4)


# 8*8 로 정답 초기화
ans = 8 * 8
# 2차원 배열 탐색
for i in range(N-7):
    for j in range(M-7):
        find_w(i,j)
        find_b(i,j)
print(ans)