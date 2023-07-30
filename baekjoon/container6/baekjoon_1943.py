# 최소공배수 = 두 수의 곱 // 최대공약수
import sys
input = sys.stdin.readline
t = int(input())

def GCD(a, b):
    while True:
        if a % b == 0:
            return b
        a, b = b, a%b


for _ in range(t):
    a, b = map(int, input().split())
    a, b = max(a,b), min(a,b)
    print(a*b // GCD(a, b))