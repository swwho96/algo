import sys
input = sys.stdin.readline
N = int(input())
dp = [(1, 0)] # 1로 끝나는, 0으로 끝나는

for _ in range(N-1):
    tmp = (dp[-1][1], dp[-1][0]+dp[-1][1])
    dp.append(tmp)

print(sum(dp[-1]))