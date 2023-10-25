import sys
import heapq
import copy
input = sys.stdin.readline
N, M, X = map(int, input().split())
village = [[] for _ in range(N+1)]

# 마을 도로 정보
for _ in range(M):
    s, e, t = map(int, input().split())
    village[s].append((e, t))

# 다익스트라 알고리즘 함수
def dijkstra(start):
    distance = [int(1e9)] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for i in village[now]:
            if cost + i[1] < distance[i[0]]:
                distance[i[0]] = cost + i[1]
                heapq.heappush(q, (cost+i[1], i[0]))
    return distance


# X에서 모든 학생에게 가는 거리
dist_from_X = dijkstra(X)
# 모든 학생 거리 확인
result = -1
for i in range(1, N+1):
    tmp = dijkstra(i)
    result = max(result, tmp[X]+dist_from_X[i])

print(result)