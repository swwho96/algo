import sys
from collections import deque, defaultdict
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    tech_tree = [0] * (n+1)
    dp = [0] * (n+1)
    time = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(k):
        pre, next = map(int, input().split())
        graph[pre].append(next)
        tech_tree[next] += 1
    w = int(input())
    q = deque()
    for i in range(1, n+1):
        if tech_tree[i] == 0:
            dp[i] = time[i]
            q.append(i)
    while q and tech_tree[w] != 0:
        now = q.popleft()
        for b in graph[now]:
            tech_tree[b] -= 1
            dp[b] = max(dp[b], dp[now]+time[b])
            if tech_tree[b] == 0:
                q.append(b)
    print(dp[w])