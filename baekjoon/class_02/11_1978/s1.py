# 1978_소수-찾기 풀이
# 2022-05-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt' , 'r')

# arr : N개의 자연수 배열
N = int(input())
arr = list(map(int, input().split()))

# 소수 판별 / 에라토스테네스의 체
cnt = 0
for num in arr:
    if num == 1:
        continue
    # num의 제곱근 범위로 충분
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            break
    else:
        cnt += 1
print(cnt)