name = list(input())
name.sort()
char_set = set()
left, mid, right = [], [], []
for char in name:
    if char not in char_set:
        char_set.add(char)
        tmp = name.count(char)
        if tmp == 1:
            mid.append(char)
            continue
        if tmp % 2 != 0:
            tmp -= 1
            mid.append(char)
        left.append(char * (tmp//2))
        right.append(char * (tmp//2))

if len(mid) >=2:
    print("I'm Sorry Hansoo")
else:
    print(''.join([*left, *mid, *right[::-1]]))