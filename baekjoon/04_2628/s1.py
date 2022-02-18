# 2628_종이자르기 풀이
# 2022-02-17

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# max() 구현하기
def my_max(para_list):
    ans = 0
    for num in para_list:
        if num > ans:
            ans = num
    return ans


# len() 구현하기
def my_len(para_list):
    ans = 0
    for i in para_list:
        ans += 1
    return ans


# sorted() 구현하기 / 버블소트
def my_sorted(para_list):
    for i in range(len(para_list)-1):
        for j in range(len(para_list)-i-1):
            if para_list[j] > para_list[j+1]:
                para_list[j], para_list[j+1] = para_list[j+1], para_list[j]
    return para_list

# N * M 행렬
M, N = map(int, input().split())

# cut_num : 짜르는 횟수
cut_num = int(input())

# cut_list : 가위 리스트
cut_list = [list(map(int,input().split())) for _ in range(cut_num)]

# cut_0 : 가로 커팅 리스트
# cut_1 : 세로 커팅 리스트
cut_0 = []
cut_1 = []

for cut in cut_list:
    
    # 가로 커팅이면 가로 커팅 리스트에 추가
    if cut[0] == 0:
        cut_0.append(cut[1])

    # 세로 커팅이면 세로 커팅 리스트에 추가
    else:
        cut_1.append(cut[1])

# 계산을 위해 각 리스트 양끝에 끝줄 값 추가
cut_0 = [0] + my_sorted(cut_0) + [N]
cut_1 = [0] + my_sorted(cut_1) + [M]

# area_list : 면적 리스트
area_list = []
for i in range(my_len(cut_0)-1):
    for j in range(my_len(cut_1)-1):

        # 각 조각들의 면적을 계산해서 리스트에 추가
        area = (cut_0[i+1]-cut_0[i]) * (cut_1[j+1]-cut_1[j])
        area_list.append(area)

# 가장 큰 면적 출력
print(my_max(area_list))