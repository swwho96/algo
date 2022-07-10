import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        each_num_count = collections.Counter(nums)
        major_time = len(nums) // 2 + 1
        for key, value in each_num_count.items():
            if value >= major_time:
                return key