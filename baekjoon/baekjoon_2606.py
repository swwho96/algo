import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited = [False for _ in range(N+1)]

while stack:
    now = stack.pop()
    if visited[now] is False:
        visited[now] = True
        stack += graph[now]

virus_computer = 0
for i in range(1, N+1):
    if visited[i] is True:
        virus_computer += 1

print(virus_computer-1 if virus_computer > 0 else virus_computer)