# 1676_팩토리얼-0의-개수 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 팩토리얼 값 구하기
def facto(number):
    if number <= 1:
        return 1
    else:
        return number * facto(number - 1)


# 입력 받기
N = int(input())

# 팩토리얼 값 구하기
num = facto(N)

# 팩토리얼 값 뒤에서 부터 0 세기
num_str = str(num)[::-1]
cnt = 0
while True:
    if num_str[cnt] == '0':
        cnt += 1
    else:
        break
print(cnt)