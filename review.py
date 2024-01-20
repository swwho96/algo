import sys
input = sys.stdin.readline

INF = int(1e9)

v, start, end, e = map(int, input().split())
edges = []

distance = [-INF] * (v + 1)

for _ in range(e):
    sv, ev, cost = map(int, input().split())
    edges.append((sv, ev, -cost))

money = list(map(int, input().split()))

def bellmanFord(start):
    distance[start] = money[start]
    for i in range(v+120):
        for j in range(e):
            curNode, nextNode, edgeCost = edges[j]
            if distance[curNode] != -INF and distance[curNode] + edgeCost + money[nextNode] > distance[nextNode]:
                distance[nextNode] = distance[curNode] + edgeCost + money[nextNode]
                if i >= v - 1:
                    distance[nextNode] = INF

bellmanFord(start)
if distance[end] == -INF: print("gg")
elif distance[end] == INF: print("Gee")
else: print(distance[end])