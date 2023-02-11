def factorial(n):
    cnt = 1
    for i in range(2, n+1):
        cnt *= i
    return cnt

n, m = map(int, input().split())
print(factorial(n) // (factorial(n-m) * factorial(m)))