n, e = map(int, input().split())
edges = []
path = [False] * (n+1)
dist = [int(1e9) for _ in range(n+1)]
dist[1] = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

# 벨만포드
for _ in range(n-1):
    for start, end, time in edges:
        if dist[start] != int(1e9) and dist[end] > dist[start] + time:
            dist[end] = dist[start] + time

# 음수 사이클 확인
flag = False
for start, end, time in edges:
    if dist[start] != int(1e9) and dist[end] > dist[start] + time:
        flag = True
        break

if flag is False:
    for i in range(2, n+1):
        if dist[i] == int(1e9):
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)