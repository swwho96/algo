def solution(s):
    answer = [char for char in s.lower()]
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i].isalpha():
            answer[i] = (s[i]).upper()
            continue
    if answer[0].isalpha():
        answer[0] = answer[0].upper()
    return ''.join(answer)