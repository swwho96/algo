N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])

# --------------------------------------------------------------

from itertools import combinations_with_replacement
N = int(input())
dp = [int(1e9)] * (N+1)
square_list = [i**2 for i in range(1, N+1) if i**2<=N]
sum_list = [sum(i) for i in combinations_with_replacement(square_list, 2)]
answer = 4
# 제곱수라면 1
if N in square_list:
    answer = 1
# 두 제곱수의 합이라면 2
elif N in sum_list:
    answer = 2
    # N-i가 두 제곱수의 합이라면 3
else:
    for j in square_list:
        if N-j in sum_list:
            answer = 3

print(answer)