import sys
K = int(sys.stdin.readline().rstrip())
money = []
for _ in range(K):
    m = int(sys.stdin.readline().rstrip())
    if m == 0:
        money.pop()
    else:
        money.append(m)
print(sum(money))