# 로또의-최고-순위와-최저-순위 풀이
# 2022-06-06


# lottos : [길이가 6인 정수 배열], 내 숫자, 0은 모름, 정렬 안되어있음
# win_nums : [길이가 6인 정수 배열], 당첨 숫자, 정렬 안되어있음
def solution(lottos, win_nums):
    # 0 개수 카운트 및 0 제거
    zero = lottos.count(0)
    new_lottos = []
    for num in lottos:
        if num != 0:
            new_lottos.append(num)

    # 0을 제외하고 맞춘 개수 계산
    match = len(new_lottos) + len(win_nums) - len(set(new_lottos + win_nums))

    # 최고 순위
    max_match = 6 - (zero + match) + 1
    if max_match == 7:
        max_match = 6

    # 최저 순위
    min_match = 6 - match + 1
    if min_match == 7:
        min_match = 6
    
    # 정답
    answer = [max_match, min_match]
    return answer