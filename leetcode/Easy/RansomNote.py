from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_cnt_dict = dict(Counter(ransomNote))
        magazine_cnt_dict = dict(Counter(magazine))
        for key, value in ransomNote_cnt_dict.items():
            if key not in magazine_cnt_dict or value > magazine_cnt_dict[key]:
                return False
        return True