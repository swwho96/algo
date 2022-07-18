import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_counter = collections.Counter(stones)
        stones_which_is_jewels = 0
        for jewel in jewels:
            if jewel in stones_counter:
                stones_which_is_jewels += stones_counter[jewel]
        return stones_which_is_jewels