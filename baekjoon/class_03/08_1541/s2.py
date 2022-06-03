# 1541_잃어버린-괄호 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 숫자랑 연산자 분리해서 리스트 만들기
def make_nums_operators():
    global input_str, nums, operators, last
    idx = 0
    now_str = input_str
    while idx != last:
        if now_str[idx] in ['+', '-']:
            operators.append(now_str[idx])
            now_str = now_str[:idx] + ' ' + now_str[idx+1:]
        idx += 1
    nums = list(map(int, now_str.split()))
    return


# 그리디
def find_ans():
    global nums, operators
    if '-' not in operators:
        return sum(nums)
    # '+'먼저 계산
    for i in range(len(operators)-1, -1, -1):
        if operators[i] == '+':
            operators.pop(i)
            nums[i] += nums.pop(i+1)
    # '+'계산 끝나고 남은 '-' 갯수 만큼 계산
    for _ in range(len(operators)):
        nums[0] -= nums.pop(1)
    return nums[0]


# 입력 받기
input_str = input()

# 숫자, 연산자 분리하기
last = len(input_str)
nums = []
operators = []
make_nums_operators()

# 그리디로 정답 찾기
ans = find_ans()
print(ans)