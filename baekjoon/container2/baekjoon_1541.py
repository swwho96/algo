import sys
input = sys.stdin.readline
x = input()
answer = int(1e9)
x = x.replace('-', ' - ').replace('+', " + ")
x = x.split()
answer = ''
flag = False
for i in x:
    if i == '-' and flag is False:
        answer += i+'('
        flag = True
    elif i == '-' and flag is True:
        flag = False
        answer += ')'+i
        answer += '('
        flag = True
    else:
        if i.isdigit():
            i = str(int(i))
        answer += i
if flag is True:
    answer += ')'
print(eval(answer))