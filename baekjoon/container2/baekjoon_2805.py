import sys
from collections import Counter
N, M, B = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

result = (99999999999999, 0)
for h in range(257):
    inventory = B
    time = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] > h:
                time += (maps[i][j] - h) * 2
                inventory += (maps[i][j] - h)
            else:
                time += h - maps[i][j]
                inventory -= h - maps[i][j]
    if inventory >= 0 and result[0] > time and result[1] < h:
        result = (time, h)

print(result[0], result[1])