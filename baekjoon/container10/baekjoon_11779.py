import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

start, end = map(int, input().split())

def dijkstra(start: int, end: int) -> tuple[str, int]:
    dists = [float('inf')] * (N + 1)
    dists[start] = 0
    # 경로 추적을 위한 리스트
    prev = [-1] * (N + 1)
    # 우선순위 큐
    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)
        
        if cost > dists[now]:
            continue
        
        for next_cost, next_node in graph[now]:
            new_cost = cost + next_cost
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
                prev[next_node] = now
    
    # 최단 경로 역추적
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    
    return ' '.join(map(str, path[::-1])), dists[end]

routs, cnt = dijkstra(start, end)
print(cnt)
print(len(routs.split()))
print(routs)