S = input()
tag = False
result, window = [], []
for char in S:
    if char == "<":
        tag = True
        result.extend(window[::-1])
        window = []
        result.append(char)
    elif char == ">":
        tag = False
        result.append(char)
    elif tag is True:
        result.append(char)
    elif char == " ":
        result.extend(window[::-1])
        window = []
        result.append(char)
    elif tag is False:
        window.append(char)

if window: result.extend(window[::-1])
print(''.join(result))