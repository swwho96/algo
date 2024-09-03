from collections import deque
N, K = map(int, input().split())

def bfs(s, e):
    prev = [-1] * 100001
    prev[s] = s
    q = deque()
    q.append((s, 0))
    while q:
        now, cnt = q.popleft()
        if now == e:
            routes = [e]
            for _ in range(cnt):
                routes.append(prev[routes[-1]])
            return cnt, reversed(routes)
        for new in [now-1, now+1, now*2]:
            if 0<=new<100001 and prev[new] == -1:
                q.append((new, cnt+1))
                prev[new] = now

if N == K:
    print(0)
    print(N)
elif N > K:
    print(N-K)
    print(*range(N, K-1, -1))
else:
    cnt, route = bfs(N, K)
    print(cnt)
    print(' '.join(map(str,route)))