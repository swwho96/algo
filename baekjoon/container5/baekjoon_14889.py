import sys
from itertools import combinations
n = int(input())
s = []
result = int(1e9)
team_div = combinations([i for i in range(n)], n//2)
total = 0
for _ in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    total += sum(a)
for combi in team_div:
    team1, team2 = 0, 0
    for a in combi:
        for b in combi:
            team1 += s[a][b]
    result = min(result, abs(total//2-team1))
print(result)