# 키패드-누르기 풀이
# 2022-06-08


# numbers : 눌러야 할 번호 리스트
# hand : 'left' - 왼손잡이 / 'right' - 오른손잡이
def solution(numbers, hand):
    # 누른 번호에 따른 위치 좌표 사전
    num_dict = {
        1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
        4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
        7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
        '*' : [3, 0], 0 : [3, 1], '#' : [3, 2],
    }

    # L_thumb : 왼손 엄지 위치 / R_thumb : 오른손 엄지 위치
    L_thumb = [3, 0]
    R_thumb = [3, 2]

    # 문자열 초기화 후 탐색 시작
    answer = ''
    for num in numbers:
        # 왼쪽 열[i, 0]의 3개의 숫자 1, 4, 7을 입력할 때는
        # 왼손 엄지손가락을 사용합니다.
        if num_dict[num][1] == 0:
            answer += 'L'
            L_thumb = num_dict[num]

        # 오른쪽 열[i, 2]의 3개의 숫자 3, 6, 9를 입력할 때는
        # 오른손 엄지손가락을 사용합니다.
        elif num_dict[num][1] == 2:
            answer += 'R'
            R_thumb = num_dict[num]

        # 가운데 열[i, 1]의 4개의 숫자 2, 5, 8, 0
        else:
            target_i, target_j = num_dict[num]
            left_i, left_j = L_thumb
            right_i, right_j = R_thumb
            L_dist = abs(left_i - target_i) + abs(left_j - target_j)
            R_dist = abs(right_i - target_i) + abs(right_j - target_j)

            # 두 엄지손가락의 현재 키패드의 위치에서
            # 더 가까운 엄지손가락을 사용합니다.
            if L_dist < R_dist:
                answer += 'L'
                L_thumb = [target_i, target_j]
            elif L_dist > R_dist:
                answer += 'R'
                R_thumb = [target_i, target_j]

            # 만약 두 엄지손가락의 거리가 같다면,
            # 오른손잡이는 오른손 엄지손가락,
            # 왼손잡이는 왼손 엄지손가락을 사용합니다.
            else:
                if hand == 'left':
                    answer += 'L'
                    L_thumb = [target_i, target_j]
                else:
                    answer += 'R'
                    R_thumb = [target_i, target_j]
    return answer