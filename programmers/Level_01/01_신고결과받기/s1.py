# 신고-결과-받기 풀이
# 2022-06-06


# id_list : 유저 ID
# report : 신고한 유저 - 신고 당한 유저
# k : 제재 기준
def solution(id_list, report, k):
    # bad_dict : (키 - 유저 : 벨류 - [해당 유저에게 신고당한 유저들])
    bad_dict = dict()
    # bad_count_dict : (키 - 신고당해본 유저 : 벨류 - 신고당한 횟수)
    bad_count_dict = dict()
    
    # report에서 하나씩 뽑아와서 dict에 기록
    for r in report:
        user, bad = r.split()
        if bad_dict.get(user) == None:
            bad_dict[user] = [bad]
            if bad_count_dict.get(bad) == None:
                bad_count_dict[bad] = 1
            else:
                bad_count_dict[bad] += 1
        else:
            if bad not in bad_dict[user]:
                bad_dict[user].append(bad)
                if bad_count_dict.get(bad) == None:
                    bad_count_dict[bad] = 1
                else:
                    bad_count_dict[bad] += 1
    
    # bad_user : 제재 대상 리스트
    bad_user = list()
    for bad in bad_count_dict:
        if bad_count_dict[bad] >= k:
            bad_user.append(bad)
    
    # 신고 처리 메일 받은 횟수 카운트
    answer = [0] * len(id_list)
    for bad in bad_user:
        for idx, user in enumerate(id_list):
            if bad_dict.get(user) == None:
                continue
            if bad in bad_dict[user]:
                answer[idx] += 1
    return answer