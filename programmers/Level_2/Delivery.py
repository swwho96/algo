import heapq
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for r in road:
        graph[r[0]].append((r[1],r[2]))
        graph[r[1]].append((r[0],r[2]))
    
    def dijkstra(s):
        q = [(0, s)]
        distance[s] = 0
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(1)
    
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer