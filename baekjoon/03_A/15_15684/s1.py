# 15684_사다리-조작 풀이
# 2022-04-17

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 사다리가 i번 세로선의 결과가 i번이 나오는지 체크하는 함수
def check():
    global ladder_map, N, H
    for n in range(1, N+1):
        start_i = 0
        start_j = n*2-2
        ni = start_i
        nj = start_j
        while True:
            if ni == 2*H:
                if start_j != nj:
                    return False
                break
            if 0 <= nj - 1 and ladder_map[ni][nj-1] == 1:
                nj -= 2
            elif nj + 1 <= 2*N - 3 and ladder_map[ni][nj+1] == 1:
                nj += 2
            ni += 1
    return True


# 사다리 조작 게임 구현하기 nCr
def game(picked, cnt):
    global ladder_map, can_make_ladder_list, r
    # 사다리 조작이 끝났으면
    if cnt == r:
        # 사다리 결과 체크
        return check()
    # 사다리 조작이 덜 끝났으면
    else:
        # nCr 조합 구현하기
        for n in range(len(can_make_ladder_list)):
            i, j = can_make_ladder_list[n]
            if cnt == 0:
                # 사다리 조작
                ladder_map[i][j] = 1
                if game(picked[:]+[n], cnt+1):
                    return True
                else:
                    # 조작했던 사다리 해제
                    ladder_map[i][j] = 0
            else:
                if n > picked[-1]:
                    # 사다리 조작
                    ladder_map[i][j] = 1
                    if game(picked[:]+[n], cnt+1):
                        return True
                    else:
                        # 조작했던 사다리 해제
                        ladder_map[i][j] = 0


# N : 세로선 개수
# M : 가로선 개수
# H : 가로층 개수
N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# 사다리 맵 만들기
ladder_map = [[1,0]*N for _ in range(2*H+1)]
for a, b in arr:
    ladder_map[2*a-1][2*b-1] = 1

# 사다리 설치 가능한 곳 리스트
can_make_ladder_list = []
for i in range(1, H+1):
    for j in range(1, N):
        if ladder_map[2*i-1][2*j-1] == 0:
            if 0 <= 2*j-3 and ladder_map[2*i-1][2*j-3] == 1:
                continue
            if 2*j+1 <= 2*N-3 and ladder_map[2*i-1][2*j+1] == 1:
                continue
            can_make_ladder_list.append((2*i-1, 2*j-1))

# r = 0에서 시작
r = 0
# r 3까지 검사, 3보다크면 -1
while r <= 3:
    if game([], 0):
        break
    r += 1

# 3보다 크면 -1
if r > 3:
    ans = -1
# 아니면 발견한 r로
else:
    ans = r
print(ans)