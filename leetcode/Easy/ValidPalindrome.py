import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', s.lower())
        if s == s[::-1]:
            return True
        else:
            return False