import sys
input = sys.stdin.readline

N, M = map(int, input().split())
distances = [float('inf')] * (N+1)
nodes = [tuple(map(int, input().split())) for _ in range(M)]


def bellman_ford(start):
    distances[start] = 0
    for v in range(N):
        for s, e, c in nodes:
            if distances[s] != float('inf') and distances[e] > distances[s] + c:
                distances[e] = distances[s] + c
                if v == N-1:
                    return False
    return True


if bellman_ford(1) is True:
    for i in range(2, N+1):
        print(distances[i] if distances[i] != float('inf') else -1)
else:
    print(-1)