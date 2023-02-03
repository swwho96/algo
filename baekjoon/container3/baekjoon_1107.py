import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
result = abs(100-N)
break_btn = set()
if M > 0:
    break_btn = set(input().split())
for i in range(1000001):
    x = str(i)
    for j in x:
        if j in break_btn:
            break
    else:
        result = min(result, abs(N-i)+len(x))
print(result)