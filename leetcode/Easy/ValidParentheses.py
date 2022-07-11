'''
(), [], {}가 올바르게 사용되었는지 검사하는 문제

1. 순서대로 사용되어야 한다
2. 열었다면 반드시 닫아야 한다.
'''
class Solution:
    def isValid(s: str) -> bool:
        bracket_sets = [0]
        check = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] not in [')', ']', '}']:
                bracket_sets.append(s[i])
            else:
                if bracket_sets.pop() != check[s[i]]:
                    return False
        return True if bracket_sets == [0] else False

print(Solution.isValid('{'))
