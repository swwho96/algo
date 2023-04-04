def solution(numbers, target):
    answer = [0]
    def dfs(combi, idx):
        if idx == len(numbers):
            if combi == target:
                answer[0] += 1
            return
        dfs(combi-numbers[idx], idx+1)
        dfs(combi+numbers[idx], idx+1)
    dfs(0, 0)
    
    return answer[0]

# ----------------------------------------------------------

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

# ----------------------------------------------------------

from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    while q:
        s, cnt = q.popleft()
        if cnt >= len(numbers):
            if s == target:
                answer += 1
        else:
            q.append((s+numbers[cnt], cnt+1))
            q.append((s-numbers[cnt], cnt+1))
    return answer