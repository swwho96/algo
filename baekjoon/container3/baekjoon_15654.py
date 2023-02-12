import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = sorted(permutations(nums, m))
for r in result:
    print(*r)