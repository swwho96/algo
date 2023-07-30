import sys
input = sys.stdin.readline

def GCD(a, b):
    while True:
        if a % b == 0:
            return b
        a, b = b, a%b

a, b = map(int, input().split())
tmp = GCD(a, b)
print('1'*tmp)