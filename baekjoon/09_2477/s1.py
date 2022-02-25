# 2477_참외밭 풀이
# 2022-02-24

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

# 회전 배열
def rotate(para_list):
    return para_list[1:] + [para_list[0]]

while True:
    # 원하는 인덱스 구조 나올 때까지 회전
    arr = rotate(arr)
    if arr[0][0] == arr[2][0] and arr[1][0] == arr[3][0]: 
        break

# 원하는 인덱스 구조에서 계산 후 출력 (큰거 - 계단형 작은거)
print((arr[4][1]*arr[5][1]-arr[1][1]*arr[2][1])*N)