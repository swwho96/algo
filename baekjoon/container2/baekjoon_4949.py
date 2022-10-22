import sys
import re
input = sys.stdin.readline
string_list = []
while True:
    char = input().rstrip()
    if char == '.':
        break
    string_list.append(re.sub('[a-zA-Z\s.]', '', char))

def bracket(char):
    bracket_dict = {')': '(', ']':'['}
    stack = [char[0]]
    for c in char[1:]:
        if len(stack) <= 0 and c in [']', ')']:
            return False
        if c in ['(', '[']: 
            stack.append(c)
        elif stack[-1] == bracket_dict[c]:
            stack.pop()
        else:
            return False
    return False if len(stack) > 0 else True


for char in string_list:
    if len(char) == 0 or bracket(char) is True:
        print('yes')
    else:
        print('no')