import sys
input = sys.stdin.readline
n, k = map(int, input().split())
luggages = [(0,0)]
check = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())
    luggages.append((w, v))

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = luggages[i][0], luggages[i][1]
        if j < w:
            check[i][j] = check[i-1][j]
        else:
            check[i][j] = max(check[i-1][j], check[i-1][j-w]+v)

print(check[n][k])