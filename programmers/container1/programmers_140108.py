def solution(s):
    answer = []
    x = s[0]
    prev = 0
    split_word = ''
    for char in s:
        if prev == 0:
            x = char
        split_word += char
        if char == x:
            prev += 1
        else:
            prev -= 1
        if prev == 0:
            answer.append(split_word)
            split_word = ''
    if split_word != '':
        answer.append(split_word)
    return len(answer)