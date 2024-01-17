import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split()) # A < B
    graph[a].append(b)
    indegree[b] += 1

# 진입차수 0인 학생 찾기
visited = [False] * (N+1)
stack = []
for i in range(1, N+1):
    if indegree[i] == 0:
        visited[i] = True
        stack.append(i)

def topology_sort(stack:list)->list:
    order = []
    while stack:
        now = stack.pop()
        order.append(str(now))
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0 and visited[i] is False:
                visited[i] = True
                stack.append(i)
    return order

result = topology_sort(stack)
print(' '.join(result))