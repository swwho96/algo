def solution(progresses, speeds):
    answer = []
    
    while len(progresses) != 0:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while (len(progresses) > 0 and progresses[0] >= 100):
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        if cnt > 0: 
            answer.append(cnt)
            
    return answer

# ----------------------------------------

from collections import deque
def solution(progresses, speeds):
    answer = []
    start = 0
    end = len(progresses)
    while start < end:
        cnt = 0
        for i in range(start, end):
            progresses[i] += speeds[i]
        while start < end:
            if progresses[start] < 100:
                break
            cnt += 1
            start += 1
        if cnt >0 : answer.append(cnt)
    return answer

# ----------------------------------------

def solution(progresses, speeds):
    answer = [0] * 100
    days = []
    for p, s in zip(progresses, speeds):
        leftover = 100 - p
        day = leftover // s if leftover % s == 0 else leftover // s + 1
        days.append(day)
    prev = 0
    for d in days:
        prev = max(prev, d)
        answer[max(prev, d)] += 1
    return [i for i in answer if i != 0]