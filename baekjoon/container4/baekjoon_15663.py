from itertools import permutations
n, m = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
result = permutations(nums, m)
visited = set()
for r in result:
    answer = ' '.join(r)
    if answer not in visited:
        visited.add(answer)
        print(answer)