import sys
N = int(sys.stdin.readline().rstrip())
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    points.append([x, y])
for x, y in sorted(points, key=lambda x: (x[1], x[0])):
    print(x, y)