'''
target값을 만들 수 있는 두 정수의 index를 반환하는 문제
'''
List = list
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i, i_num in enumerate(nums):
            for j, j_num in enumerate(nums):
                if i_num + j_num == target:
                    return [i, j]

print(Solution.twoSum(nums = [2,7,11,15], target = 9))