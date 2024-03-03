import sys
input = sys.stdin.readline

a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

sub_text = []
p, q = len(a), len(b)
while True:
    if p == 0 or q == 0:
        break
    if a[p-1] == b[q-1]:
        sub_text.append(a[p-1])
        p, q = p-1, q-1
    else:
        if dp[p-1][q] > dp[p][q-1]:
            p, q = p-1, q
        else:
            p, q = p, q-1


print(dp[-1][-1])
print(''.join(sub_text[::-1]))