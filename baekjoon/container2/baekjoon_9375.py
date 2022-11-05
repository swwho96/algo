import sys
from collections import Counter
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    clothes = []
    k = int(sys.stdin.readline().rstrip())
    
    for _ in range(k):
        c, name = sys.stdin.readline().split()
        clothes.append(name)
    cnt = Counter(clothes)
    matches = 1
    for kind_cnt in cnt.values():
        matches *= kind_cnt + 1
    print(matches-1)