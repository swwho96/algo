def solution(cards):
    answer = []
    visited = [False] * len(cards)
    
    def dfs(num:int):
        cnt = 0
        cur = num
        while visited[cur] is False:
            visited[cur] = True
            cnt += 1
            cur = cards[cur] - 1
        return cnt
    
    for i in range(len(cards)):
        if visited[i] is False:
            answer.append(dfs(i))
    answer.sort()
    return answer[-1]*answer[-2] if len(answer) > 1 else 0