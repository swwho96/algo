from collections import deque
def isBracketCorrect(s):
    bracket_dict = {']':'[', '}':'{', ')':'('}
    check_list = []
    for char in s:
        if char in bracket_dict.keys():
            if len(check_list) <= 0 or check_list[-1] != bracket_dict[char]:
                return False
            else:
                check_list.pop()
        else:
            check_list.append(char)
    return True if len(check_list) == 0 else False
                
        
def solution(s):
    answer = 0
    q = deque(s)
    for _ in range(len(s)):
        q.rotate(-1)
        if isBracketCorrect(q) is True:
            answer += 1
    return answer