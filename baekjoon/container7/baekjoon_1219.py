import sys

# 입력받기
n, S, E, m = map(int, input().split())
board = []
for _ in range(m):
    a, b, c = map(int, input().split())
    board.append((a,b,c))

INF = int(1e9)
distance = [-INF] * n

citymoney = list(map(int, input().split()))

distance[S] = citymoney[S]

for i in range(n+100):
    for s, e, p in board:
        if distance[s] != -INF:
            if distance[s] == INF:
                distance[e] = INF
            elif distance[e] < distance[s] + citymoney[e] - p:
                distance[e] = distance[s] + citymoney[e] - p
                if i >= n-1:
                    distance[e] = INF

if distance[E] == -INF:
    print('gg')
elif distance[E] == INF:
    print('Gee')
else:
    print(distance[E])