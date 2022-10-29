import sys
N, K = map(int, sys.stdin.readline().split())
moneys = sorted(list(map(int,sys.stdin.read().splitlines())), reverse=True)
cnt = 0
for m in moneys:
    if K == 0:
        break
    else:
        cnt += K // m
        K %= m
print(cnt)