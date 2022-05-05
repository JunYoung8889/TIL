# 1157_단어-공부 풀이
# 2022-05-05

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 대문자로 통일
word = input().upper()
# 문자 개수 딕셔너리 만들기
word_dict = dict()
for char in word:
    if word_dict.get(char) == None:
        word_dict[char] = 1
    else:
        word_dict[char] += 1
# 문자가 가장 많이 나온 횟수
max_num = max(word_dict.values())
# 가장 많이 나온 문자 변수 초기화
max_char = ''
for char in word_dict:
    if word_dict[char] == max_num:
        # 유일한 문자가 아니면
        if max_char != '':
            print('?')
            break
        max_char = char
else:
    print(max_char)