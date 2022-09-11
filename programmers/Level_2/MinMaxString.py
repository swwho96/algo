def solution(s):
    answer = ''
    number_list = list(map(int, s.split()))
    answer += str(min(number_list)) + ' ' + str(max(number_list))
    return answer