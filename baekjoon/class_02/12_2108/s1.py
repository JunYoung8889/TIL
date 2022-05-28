# 2108_통계학 풀이
# 2022-05-28

'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N : 홀수 / arr : N개의 정수 배열
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 산술평균
print(round(sum(arr)/N))

# 중앙값
print(arr[N//2])

# 최빈값
cnt_dict = dict()
for num in arr:
    if cnt_dict.get(num) == None:
        cnt_dict[num] = 1
    else:
        cnt_dict[num] += 1
max_cnt_list = list(filter(lambda x: cnt_dict[x] == max(cnt_dict.values()), cnt_dict))
if len(max_cnt_list) > 1:
    max_cnt_list.sort()
    print(max_cnt_list[1])
else:
    print(max_cnt_list[0])

# 범위
print(max(arr) - min(arr))