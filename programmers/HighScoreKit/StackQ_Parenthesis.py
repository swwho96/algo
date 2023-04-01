def solution(s):
    if len(s) == 0:
        return True
    answer = True
    check_list = []
    for parenthesis in s:
        if parenthesis == '(':
            check_list.append(parenthesis)
        else:            
            if len(check_list) == 0:
                return False
            elif check_list[-1] == ')':
                return False
            elif check_list[-1] == '(':
                check_list.pop()
    return True if len(check_list) == 0 else False

# ---------------------------------------------------

def solution(s):
    check = 0
    for char in s:
        check += 1 if char == '(' else -1
        if check < 0:
            return False
    return True if check == 0 else False