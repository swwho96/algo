import sys
input = sys.stdin.readline
n = int(input())
fees = []
for _ in range(n):
    fees.append(list(map(int, input().split())))
for i in range(1, n):
    fees[i][0] += min(fees[i-1][1], fees[i-1][2])
    fees[i][1] += min(fees[i-1][0], fees[i-1][2])
    fees[i][2] += min(fees[i-1][0], fees[i-1][1])
print(min(fees[-1]))