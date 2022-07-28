def solution(s):
    s_stack = [s[0]]
    for char in s[1:]:
        if len(s_stack) >= 1 and s_stack[-1] == char:
            s_stack.pop()
        else:
            s_stack.append(char)

    return 1 if len(s_stack) == 0 else 0