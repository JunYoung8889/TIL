# 14500_테트로미노 풀이
# 2022-03-29

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 재귀함수로 구현하기
# idx_list : 방문한 인덱스 [i,j]들을 담을 리스트
# sums : 해당 경로의 합계
# cnt : 방문한 개수
def tetro(i, j, idx_list, sums, cnt):
    global arr, N, M, max_ans
    # 가지치기
    # 예를들어 현재 최대값이 3500이면
    # 첫칸에 500이하가 들어오면 볼필요도 없다.
    if sums <= max_ans - 1000*(4-cnt):
        return
    # 인덱스 범위를 벗어났으면
    if i < 0 or i >= N or j < 0 or j >= M:
        # 탐색 종료
        return
    # 인덱스 범위를 만족하면
    else:
        # 이미 방문했으면
        if [i,j] in idx_list:
            # 탐색종료
            return
        # 방문한적 없으면
        else:
            # 현재 합계에 더해주기
            sums += arr[i][j]
            # 방문 개수 증가
            cnt += 1
            # 방문 리스트에 추가
            idx_list = idx_list[:] + [[i,j]]
    # 4개 방문 완료 했으면
    if cnt == 4:
        # 해당 합계와 최대치 비교
        if sums > max_ans:
            # 갱신 하기
            max_ans = sums
        # 탐색 종료
        return
    # 방문 완료 안했으면
    else:
        # 현재까지 방문했던 인덱스 리스트에서 인덱스 하나씩 뽑아오기
        for i, j in idx_list:
            # 해당 블럭 아래 방향에 블럭 추가
            tetro(i+1, j, idx_list, sums, cnt)
            # 해당 블럭 오른쪽 방향에 블럭 추가
            tetro(i, j+1, idx_list, sums, cnt)
            # 해당 블럭 위 방향에 블럭 추가
            tetro(i-1, j, idx_list, sums, cnt)
            # 해당 블럭 왼쪽 방향에 블럭 추가
            tetro(i, j-1, idx_list, sums, cnt)
        # 탐색 종료
        return


# arr : N * M 행렬
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 합계 초기화
max_ans = 0
# 2차원 배열 탐색
for i in range(N):
    for j in range(M):
        tetro(i, j, [], 0, 0)
print(max_ans)