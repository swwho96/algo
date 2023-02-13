import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = combinations_with_replacement(nums, m)
for r in result:
    print(*r)