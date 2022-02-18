# 양의 정수 N 입력받기
N = int(input())

# max_cnt : 최대 개수
max_cnt = 0

# 두번째 숫자 i 는 0 ~ N
# for i in range(N+1):
for i in range(int(0.617*N),int(0.619*N)+2):

    # nums : 숫자들을 입력받을 리스트
    nums = [N,i]

    # num : 다음에 추가할 숫자
    # j : 확인할 인덱스
    # cnt : 원소 개수
    num = N - i
    j = 1
    cnt = 2

    # 음수가 나오면 추가하지 않고 종료
    while num >= 0:

        # 원소 추가하고 cnt 카운트 1 증가
        nums.append(num)
        cnt += 1

        # 규칙에 따라 다음에 추가할 숫자 갱신
        num = nums[j] - nums[j+1]

        # 확인할 인덱스 1 증가
        j += 1

    # 최대 개수, 최대 숫자 리스트 갱신
    if cnt > max_cnt:
        max_cnt = cnt
        max_nums = nums

# 출력
print(max_cnt)
for i in range(max_cnt):

    # 마지막 숫자이면
    if i == max_cnt-1:

        # 숫자 출력 후 줄바꿈
        print(max_nums[i])

    # 마지막 숫자가 아니면
    else:

        # 숫자 출력 후 공백출력
        print(max_nums[i], end = ' ')