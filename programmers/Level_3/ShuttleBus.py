from bisect import bisect_right
def solution(n, t, m, timetable):
    answer = ''
    nowtime = 540
    timetable = sorted([int(t[:2])*60 + int(t[3:]) for t in timetable])
    while n > 0:
        if n == 1:
            print(nowtime, timetable, m)
            if bisect_right(timetable, nowtime) >= m:
                answer = timetable[m-1] - 1
            else:
                answer = nowtime
            break
        idx = bisect_right(timetable, nowtime)
        if idx >= m:
            timetable = timetable[m:]
        else:
            timetable = timetable[idx:]
        nowtime += t
        n -= 1
    answer = str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)
    return answer