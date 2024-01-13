from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
lcm = 1
D = [0] * N
visited = [False] * N

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i[0]] is False:
                D[i[0]] = D[now] * i[2]//i[1]
                visited[i[0]] = True
                q.append(i[0])
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b,p,q))
    graph[b].append((a,p,q))
    lcm *= (p*q // gcd(max(p,q), min(p,q)))


D[0] = lcm
bfs(0)
mgcd = D[0]

for i in range(1, N):
    mgcd = gcd(max(mgcd, D[i]), min(mgcd, D[i]))

for i in range(N):
    print(int(D[i] // mgcd), end=' ')