List=list
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone_table = {
            2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
        }
        
        n = []
        for dig in digits:
            n.append(phone_table[int(dig)])
            
        return [''.join(combi) for combi in list(product(*n))]
        

s = Solution()
print(s.letterCombinations('2'))