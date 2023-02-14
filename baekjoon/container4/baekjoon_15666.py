from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())), key=int)
result = sorted(set(combinations_with_replacement(nums, m)))
for r in result:
    print(' '.join(map(str, r)))