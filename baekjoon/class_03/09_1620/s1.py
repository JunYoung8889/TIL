# 1620_나는야-포켓몬-마스터-이다솜 풀이
# 2022-06-03

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 입력 받기
N, M  = map(int, input().split())
pokemon_list = [input() for _ in range(N)]
my_find_list = [input() for _ in range(M)]

# 포켓몬 도감 딕셔너리로 만들기
name_dict = dict()
nums_dict = dict()
for idx, pokemon in enumerate(pokemon_list):
    name_dict[pokemon] = idx + 1
    nums_dict[str(idx+1)] = pokemon

# 찾기
for my_find in my_find_list:
    if name_dict.get(my_find) != None:
        print(name_dict[my_find])
    else:
        print(nums_dict[my_find])