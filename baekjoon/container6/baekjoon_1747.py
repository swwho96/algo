n = int(input())

# 소수 판별
def isPrime(x:int):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

# 팰린드롬 판별
def palindrome(x:int):
    x = str(x)
    l, r = 0, len(x)-1
    while (l<r):
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True

i = n
while True:
    if i != 1 and isPrime(i) is True and palindrome(i) is True:
        print(i)
        break
    i += 1