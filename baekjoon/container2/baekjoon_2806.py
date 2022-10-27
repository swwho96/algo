import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))
trees = Counter(trees)
h_mean = (sum(trees) // N)
start, end = (h_mean - M//N), max(trees)
while start <= end:
    can_take_tree = 0
    mid = (start + end) // 2
    for t, cnt in trees.items():
        if t > mid:
            can_take_tree += (t - mid) * cnt
    if can_take_tree >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)