import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
distances = [float('inf')] * (N+1)
distances[1] = 0
board = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))

q = []
heapq.heappush(q, (1, 0))
while q:
    s, cost = heapq.heappop(q)
    if distances[s] < cost:
        continue
    for next, new_cost in board[s]:
        if distances[next] > distances[s] + new_cost:
            distances[next] = distances[s] + new_cost
            heapq.heappush(q, (next, distances[next]))

print(distances[N])