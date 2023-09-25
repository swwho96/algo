from collections import defaultdict
def solution(s):
    INF = int(1e9)
    answer = INF
    n = len(s)
    for i in range(1, n+1):
        tmp = ''
        prev = s[:i]
        cnt = 1
        for idx in range(i, n, i):
            now = s[idx:idx+i]
            if prev == now:
                cnt += 1
            else:
                tmp += str(cnt)+prev if cnt > 1 else prev
                cnt = 1
                prev = now
        tmp += str(cnt)+prev if cnt > 1 else prev
        if answer > len(tmp):
            answer = len(tmp)
    return answer



def solution(s):
    min_len = len(s)
    for cnt in range(1, len(s)//2+1):
        tmp = [s[i:i+cnt] for i in range(0, len(s), cnt)]
        prev, prev_cnt = tmp[0], 1
        tmp_result = []
        for char in tmp[1:]:
            if prev == char:
                prev_cnt += 1
            else:
                if prev_cnt > 1:
                    tmp_result.append(str(prev_cnt))
                tmp_result.append(prev)
                prev = char
                prev_cnt = 1
        if prev_cnt > 1:
            tmp_result.append(str(prev_cnt))
        tmp_result.append(char)
        tmp_result = ''.join(tmp_result)
        if min_len > len(tmp_result):
            min_len = len(tmp_result)
    return min_len


def solution(s):
    min_len = len(s)
    for cnt in range(1, len(s)//2+1):
        prev, prev_cnt = s[:cnt], 1
        tmp_result = 0
        for i in range(cnt, len(s), cnt):
            char = s[i:i+cnt]
            if prev == char:
                prev_cnt += 1
            else:
                tmp_result += (len(prev) + len(str(prev_cnt))) if prev_cnt > 1 else len(prev)
                prev = char
                prev_cnt = 1
        tmp_result += (len(prev) + len(str(prev_cnt))) if prev_cnt > 1 else len(prev)
        if min_len > tmp_result:
            min_len = tmp_result
    return min_len