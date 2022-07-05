class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = {}
        for i in s:
            if i in s_cnt:
                s_cnt[i] += 1
            else:
                s_cnt[i] = 1
        for j in t:
            if j in s_cnt:
                s_cnt[j] -= 1
            else:
                return False
        if min(s_cnt.values()) == 0 and max(s_cnt.values()) == 0:
            return True
        else:
            return False
