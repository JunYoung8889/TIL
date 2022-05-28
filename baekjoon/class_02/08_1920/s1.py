# 1920_수-찾기 풀이
# 2022-05-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 자연수 N, M / N, M개의 정수 배열 arr1, arr2
N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))

# 이분 탐색
for num2 in arr2:
    start = 0
    end = N-1
    while True:
        # 발견 못함
        if start > end:
            print(0)
            break
        
        middle = start + (end - start)//2
        
        # 발견
        if arr1[middle] == num2:
            print(1)
            break
        
        # 좌측 부분으로 범위 줄이기
        elif arr1[middle] > num2:
            end = middle - 1
        
        # 우측 부분으로 범위 줄이기
        elif arr1[middle] < num2:
            start = middle + 1