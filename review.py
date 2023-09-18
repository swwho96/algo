import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
bus_info = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if bus_info[a][b] > c: 
        bus_info[a][b] = c

# 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    bus_info[i][i] = 0

# 버스 정보 업데이트
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus_info[i][j] = min(bus_info[i][j], bus_info[i][k]+bus_info[k][j])

# 정보 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if bus_info[i][j] == INF:
            print(0, end=' ')
        else:
            print(bus_info[i][j], end=' ')
    print()