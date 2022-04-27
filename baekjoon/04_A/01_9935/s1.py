# 9935_문자열-폭발 풀이
# 2022-04-26
# python3 : 1148ms / pypy3 : 272ms

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')


# 탐색
def game(input_list, boomb, input_list_cnt, boomb_cnt):
    # 초기화
    check_list = input_list[:boomb_cnt]
    # i : input_list의 idx
    i = boomb_cnt-1
    # top : check_list 의 꼭대기
    top = boomb_cnt-1
    while i != input_list_cnt:
        # check_list가 boomb보다 짧으면
        # boomb 길이만큼 될 때까지 append
        if top < boomb_cnt-1:
            while top != boomb_cnt-1:
                i += 1
                if i == input_list_cnt:
                    break
                check_list.append(input_list[i])
                top += 1
            if i == input_list_cnt:
                break
        # 패턴 비교
        for j in range(boomb_cnt):
            # 한글자씩 비교 하다가 패턴이 다르다고 판단하면
            if check_list[top-boomb_cnt+1 + j] != boomb[j]:
                i += 1
                if i == input_list_cnt:
                    break
                # 문자 하나 추가하고 현재 패턴 비교 종료
                check_list.append(input_list[i])
                top += 1
                break
        # 패턴이 일치하면
        else:
            # boomb 길이만큼 pop
            for _ in range(boomb_cnt):
                check_list.pop()
                top -= 1
    # 탐색을 마친 후 빈 리스트 이면
    if check_list == []:
        return 'FRULA'
    else:
        return ''.join(check_list)


# 입력 받기, str은 불변 이므로 list로 입력받기
input_list = list(input())
input_list_cnt = len(input_list)
boomb = list(input())
boomb_cnt = len(boomb)
# 탐색
ans = game(input_list, boomb, input_list_cnt, boomb_cnt)
print(ans)