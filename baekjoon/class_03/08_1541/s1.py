# 1541_잃어버린-괄호 풀이
# 2022-06-03

import sys
sys.stdin = open('input.txt', 'r')
input= sys.stdin.readline


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


def find_ans(now_nums, now_ops, cnt):
    global min_ans, op_cnt
    if '-' not in now_ops:
        ans = sum(now_nums)
        if ans < min_ans:
            min_ans = ans
        return
    if cnt == op_cnt:
        if now_nums[0] < min_ans:
            min_ans = now_nums[0]
        return
    old_nums = now_nums[:]
    old_ops = now_ops[:]
    for i in range(len(now_ops)):
        if now_ops[i] == '+':
            now_ops.pop(i)
            now_nums[i] += now_nums.pop(i+1)
            find_ans(now_nums, now_ops, cnt + 1)
            now_nums = old_nums[:]
            now_ops = old_ops[:]
        else:
            now_ops.pop(i)
            now_nums[i] -= now_nums.pop(i+1)
            find_ans(now_nums, now_ops, cnt + 1)
            now_nums = old_nums[:]
            now_ops = old_ops[:]


input_str = input()
last = len(input_str)
nums = []
operators = []
make_nums_operators()
op_cnt = len(operators)
min_ans = sum(nums)
find_ans(nums[:], operators[:], 0)
print(min_ans)