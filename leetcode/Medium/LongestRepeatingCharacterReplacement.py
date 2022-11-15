from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = Counter()
        maxlen = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            cur_len = r - l + 1
            if cur_len - freq.most_common(1)[0][1] <= k:
                maxlen = max(maxlen, cur_len)
            else:                               
                freq[s[l]] -= 1                 
                l += 1
        return maxlen