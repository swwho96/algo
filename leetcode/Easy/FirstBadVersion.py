'''
테스트를 위한 코드입니다.
bad = 1

def isBadVersion(version):
    if version >= bad:
        return True
    else:
        return False'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left+right) // 2
            if isBadVersion(mid) is True:
                if isBadVersion(mid-1) is False:
                    return mid
                else:
                    right = mid
            else:
                left = mid+1
        return left


s = Solution()
print(s.firstBadVersion(1))