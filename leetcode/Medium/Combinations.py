# 조합 활용
from itertools import combinations
def combine(self, n: int, k: int) -> List[List[int]]:
    n_list = [i for i in range(1,n+1)]
    return list(combinations(n_list, k))

# DFS 활용
def combine(n, k):
    nums = [i for i in range(1, n+1)]
    result = []
    stack = [[0, nums, []]]
    while stack:
        length, integers, ans = stack.pop()
        if length == k:
            result.append(ans)
        else:
            for i in range(len(integers)):
                stack.append([length+1, integers[i+1:], ans+[integers[i]]])
    return result