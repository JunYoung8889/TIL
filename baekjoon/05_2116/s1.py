# 2116_주사위_쌓기 풀이
# 2022-02-18

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


# N : 주사위 개수
N = int(input())

# dices : 주사위들 리스트
dices = [list(map(int, input().split())) for _ in range(N)]

# match_list : 마주보고 있는 인덱스
match_list = [5,3,4,1,2,0]

# cnts : 총합들 리스트
cnts = []
for i in range(1,7):

    # cnt : 총합
    # bottom : 밑면 숫자
    cnt = 0
    bottom = i
    for dice in dices:
        for j in range(6):
            if dice[j] == bottom:

                # top : 윗면 숫자
                top = dice[match_list[j]]

        # 윗면 아랫면 5, 6 / 6, 5 이면
        if bottom * top == 30:

            # 최대 숫자는 5, 6을 제외한 4이다.
            cnt += 4
        
        # 밑면 또는 아랫면 6 이면
        elif bottom == 6 or top == 6:

            # 최대 숫자는 6을 제외한 5이다.
            cnt += 5

        # 그외에는 최대 숫자는 6이다.
        else:
            cnt += 6
        
        # 다음 주사위의 밑면은 아래 주사위의 윗면이다.
        bottom = top
    
    # 총합 리스트에 총합 추가
    cnts.append(cnt)

# 총합 리스트에서 최대값 찾기
ans = my_max(cnts)
print(ans)