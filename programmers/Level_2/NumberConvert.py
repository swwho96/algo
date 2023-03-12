from collections import deque
def solution(x, y, n):
    answer = -1
    q = deque([(0,x)])
    while q:
        cnt, x = q.popleft()
        if x == y:
            answer = cnt
            break
        if x * 3 <= y:
            q.append((cnt+1, x*3))
        if x * 2 <= y:
            q.append((cnt+1, x*2))
        if x+n <= y:
            q.append((cnt+1, x+n))            
    return answer


# _____________________________________________

def solution(x, y, n):
    INF = int(1e9)
    dp = [INF] * (y+1)
    dp[x] = 0
    for i in range(x, y+1):
        if i*3 <= y:
            dp[i*3] = min(dp[i*3], dp[i]+1)
        if i*2 <= y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i+n <= y:
            dp[i+n] = min(dp[i+n], dp[i]+1)
    return dp[y] if dp[y] != INF else -1