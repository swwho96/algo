import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readlines

def cantor(string, n):
    if n == 1:
        return string
    return cantor(string[:(n//3)], n//3) + [' ']*(n//3) + cantor(string[-(n//3):], n//3)

lines = input()
for line in lines:
    N = int(line.rstrip())
    print(cantor(['-'] * (3 ** N)), N)