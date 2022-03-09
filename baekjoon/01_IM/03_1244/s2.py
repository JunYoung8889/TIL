# 1244_스위치_켜고_끄기 풀이2
# 2022-02-27

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# N : 스위치 개수
# arr : 스위치 1차원 배열
# stu_num : 학생 수
# studuents : 학생 2차원 배열
N = int(input())
arr = list(map(int, input().split()))
stu_num = int(input())
students = [list(map(int, input().split())) for _ in range(stu_num)]

# 학생들 리스트에서 학생 한명씩 뽑아와서 검사
for student in students:
    # 남학생 이면
    if student[0] == 1:
        # k : 학생이 받은 숫자
        # k * n 번 스위치를 바꿔주는데 인덱스라서 -1씩 해준다.
        k = student[1]
        n = 1
        while k*n - 1 < N:
            arr[k*n-1] = (arr[k*n-1] + 1) % 2
            n += 1

    # 여학생 이면
    else:
        # k : 학생이 받은 숫자
        k = student[1]
        # 일단 그 숫자 -1 인덱스 의 스위치 상태 변경
        arr[k-1] = (arr[k-1] + 1) % 2
        # 1칸씩 늘려가면서 양옆 비교
        n = 1
        while 0 <= k-1-n < N and 0 <= k-1+n < N:
            # 대칭 이면
            if arr[k-1-n] == arr[k-1+n]:
                # 상태 변경
                arr[k-1-n] = (arr[k-1-n] + 1) % 2
                arr[k-1+n] = (arr[k-1+n] + 1) % 2
            # 대칭이 아니면 탐색 종료
            else:
                break
            n += 1

# 한줄에 20개씩 출력하는 형식
for i in range(0,N,20):
    print(*arr[i:i+20])