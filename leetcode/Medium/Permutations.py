List = list
from itertools import combinations, permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[*permut] for permut in list(permutations(nums, len(nums)))]

s = Solution()
print(s.permute([1,2,3]))