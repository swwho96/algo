from itertools import combinations
List = list
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n_list = [i for i in range(1,n+1)]
        return list(combinations(n_list, k))
