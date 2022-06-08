# 숫자-문자열과-영단어 풀이
# 2022-06-08

def solution(s):
    # num_dict : (키 - 영단어 : 벨류 - 숫자)
    num_dict = {
        'zero' : '0', 'one' : '1', 'two' : '2',
        'three' : '3', 'four' : '4', 'five' : '5',
        'six' : '6', 'seven' : '7', 'eight' : '8',
        'nine' : '9',
    }
    for num in num_dict:
        if num in s:
            # str.replace(str1, str2)
            # 문자열 변수 str에 포함된 str1을 str2로 대체
            s = s.replace(num, num_dict[num])

    # 출력 형식에 맞춰 int로 변환
    answer = int(s)
    return answer