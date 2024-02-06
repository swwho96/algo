import sys
input = sys.stdin.readline

N = int(input())

a, b = 0, 1
for i in range(3, N+1):
    new = (i-1) * (a + b) % 1000000000
    a = b
    b = new

print(b if N > 1 else 0)