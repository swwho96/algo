n = int(input())
a = list(map(int, input().split()))
dp = [[a[i]] for i in range(n)]

for i in range(1, len(a)):
    num = a[i]
    for j in range(0, i):
        if a[j] < num and len(dp[i]) <= len(dp[j]):
            dp[i] = dp[j] + [num]

print(dp)
answer = max(dp, key = len)
print(len(answer))
print(* answer)