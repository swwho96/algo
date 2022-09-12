def solution(n):
    answer = 0
    fib = [0,1]
    for i in range(2,n+1):
        fib += [fib[i-1] + fib[i-2]]
    return fib[n] % 1234567