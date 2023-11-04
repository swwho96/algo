from collections import deque
string = input()
stack = []
result = []
for char in string:
    if char.isalpha():
        result.append(char)
    elif char == '(':
        stack.append(char)
    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result.append(stack.pop())
        stack.append(char)
    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(char)
    else:
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    # print('stack', result, stack)
    
while stack:
    result.append(stack.pop())

print(''.join(result))