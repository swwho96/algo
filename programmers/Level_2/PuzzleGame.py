def solution(diffs, times, limit):
    n = len(diffs)
    left, right = 1, max(diffs)
    while left < right:
        tmp_time = 0
        level = (left+right) // 2
        for i in range(n):
            if level >= diffs[i]:
                tmp_time += times[i]
            else:
                tmp_time += (times[i]+times[i-1])*(diffs[i]-level) + times[i]
        if tmp_time == limit:
            right = level
            break
        elif tmp_time >= limit:
            left = level+1
        else:
            right = level
    return right