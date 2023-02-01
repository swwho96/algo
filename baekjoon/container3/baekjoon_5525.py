import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()
cnt = 0
result = 0
i = 1
while i < m-1:
    if s[i-1]+s[i]+s[i+1] == 'IOI':
        cnt += 1
        if cnt == n:
            cnt -= 1
            result += 1
        i += 2
        continue
    i += 1
    cnt = 0
print(result)