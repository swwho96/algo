from itertools import combinations
n, m = map(int, input().split())
result = sorted(list(combinations([i for i in range(1, n+1)], m)))
for r in result:
    print(*r)