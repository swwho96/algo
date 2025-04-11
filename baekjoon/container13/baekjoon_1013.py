import re
import sys
input = sys.stdin.readline

T = int(input().rstrip())
r = re.compile("(100+1+|01)+")
for _ in range(T):
    pattern = input().rstrip()
    if r.fullmatch(pattern) is not None:
        print('YES')
    else:
        print('NO')
