# 5052_전화번호-목록 풀이
# 2022-04-28
# python3 : 시간초과 / pypy3 : 3612ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 패턴 분석 함수
def game():
    global N, arr
    # 완탐
    for i in range(N-1):
        for j in range(i+1,N):
            # 문자 하나씩 비교
            for k in range(len(arr[i])):
                # 다른문자 발견
                if arr[i][k] != arr[j][k]:
                    break
            # 패턴 일치
            else:
                return 'NO'
    return 'YES'


# 테스트 케이스 입력받기
T = int(input())
for t in range(1, T+1):
    # arr : N개의 전화번호 리스트
    N = int(input())
    arr = [input() for _ in range(N)]
    # 문자열 길이를 기준으로 정렬
    arr.sort(key=len)
    ans = game()
    print(ans)