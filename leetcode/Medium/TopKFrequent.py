import collections
List = list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frq = collections.Counter(nums)
        answer = [common[0] for common in num_frq.most_common(n=2)]
        print(answer)
        # return answer


s = Solution()
print(s.topKFrequent([1,1,1,1,2,2,2,3,3,3], k=2))