from math import gcd, lcm

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

'''
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)
'''
