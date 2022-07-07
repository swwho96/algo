class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        method_list = [1,2] + [0 for _ in range(2,n)]
        for i in range(2, n):
            method_list[i] = method_list[i-1] + method_list[i-2]
        return method_list[-1]

s = Solution()
print(s.climbStairs(38))