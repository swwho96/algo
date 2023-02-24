from collections import deque
n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    visited = [1] * 200001
    q = deque([(0, n)])
    while q:
        cnt, now = q.popleft()
        if now == k:
            print(cnt)
            break
        if now*2 <= 200000 and visited[now*2]:
            visited[now*2] = 0
            q.append((cnt, now*2))
        if now-1 >= 0 and visited[now-1]:
            visited[now-1] = 0
            q.append((cnt+1, now-1))
        if now+1 <= 100000 and visited[now+1]:
            visited[now+1] = 0
            q.append((cnt+1, now+1))