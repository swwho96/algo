from bisect import bisect_left
List = list
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if len(nums) > idx and nums[idx] == target:
            return idx
        else:
            return -1
