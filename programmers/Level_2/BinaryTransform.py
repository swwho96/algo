def solution(s):
    answer = []
    trans_cnt, zero_cnt = 0, 0
    x = s
    while x != '1':
        zero_cnt += x.count('0') # +0개수
        x = "1" * x.count('1') # 0 제거
        x = format(len(x), 'b') # x의 길이를 2진법으로 변환
        trans_cnt += 1 # 이진변환 +1
    answer = [trans_cnt, zero_cnt]
    return answer