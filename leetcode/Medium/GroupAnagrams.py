import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagram_dict = collections.defaultdict(list)
        for word in strs:
            group_anagram_dict[''.join(sorted(word))].append(word)
        return group_anagram_dict.values()