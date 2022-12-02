# 조합 활용
from itertools import combinations, permutations
def permute(self, nums: List[int]) -> List[List[int]]:
    return [[*permut] for permut in list(permutations(nums, len(nums)))]

# DFS 활용
def permute(self, nums):
    res = []
    n = len(nums)
    stack = [[0, nums, []]]
    while stack:
        length, integers, ans = stack.pop()
        if length == n:
            res.append(ans)
        else:
            for i in range(len(integers)):
                stack.append([length+1, integers[:i]+integers[i+1:], ans+[integers[i]]])
    return res