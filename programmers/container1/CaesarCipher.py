def solution(s, n):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if 'a'<= i <= 'z':
            changed = alpha[(alpha.index(i)+n) % 26]
        else:
            changed = alpha[(alpha.index(i.lower())+n) % 26].upper()
        answer += changed
    return answer

# ----------------------------------------------------------------------

def solution(s, n):
    answer = []
    for alpha in s:
        if alpha != " ":
            if alpha.islower():
                alpha = chr((ord(alpha) + n - 97) % 26 + 97)
            elif not alpha.islower():
                alpha = chr((ord(alpha) + n - 65) % 26 + 65)
        answer.append(alpha)
    return ''.join(answer)