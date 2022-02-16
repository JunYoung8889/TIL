# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N_sw : 스위치 개수
N_sw = int(input())

# nums : 스위치 1,0 리스트 / 인덱스 에러방지, 대칭비교 방지 [2] 추가
nums = [2] + list(map(int, input().split())) + [2]

# N_st : 학생수
N_st = int(input())
for i in range(N_st):

    # BG / Boy = 1 Girl =2
    # num : 학생이 받은 숫자
    BG,num = map(int,input().split())

    # 남학생 이면
    if BG == 1:

        # num에서 시작해서 배수 찾기
        for j in range(num,N_sw+1,num):

            # 1이면 0으로 0이면 1로 상태변화
            nums[j] = (nums[j]+1)%2

    # 여학생 이면
    else:

        # num에서 1이면 0으로 0이면 1로 상태변화
        nums[num] = (nums[num]+1)%2

        # k를 1부터 증가시키면서 대칭비교
        k = 1

        # 대칭이면
        while nums[num+k] == nums[num-k]:

            # 1이면 0으로 0이면 1로 상태변화
            nums[num+k] = (nums[num+k]+1)%2
            nums[num-k] = (nums[num-k]+1)%2

            # k 1증가 후 다시 대칭비교
            k += 1

# 한줄에 20개씩 출력!
for i in range(1,N_sw+1):
    if i%20 == 0:
        print(nums[i])
    else:
        print(nums[i], end = ' ')