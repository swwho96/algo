from itertools import combinations_with_replacement
n, m = map(int, input().split())
result = sorted(list(combinations_with_replacement([i for i in range(1,n+1)], m)))
for r in result:
    print(*r)