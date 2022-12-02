# 조합 활용
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: # digit이 없을 때 예외처리
            return []
        
        phone_table = {
            2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
        }
        
        # n에 digit에 적힌 알파벳 리스트로 담기
        n = []
        for dig in digits:
            n.append(phone_table[int(dig)])
        
        
        return [''.join(combi) for combi in list(product(*n))]


# DFS - while 활용
def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
    
    phone_table = {
        2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
    }

    result = []
    stack = [(0, [])]

    while stack:
        index, chars = stack.pop()
        if index == len(digits):
            result.append("".join(chars))
        else:
            for char in phone_table[int(digits[index])]:
                stack.append([index+1, chars + [char]])
    return result


