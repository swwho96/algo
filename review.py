import sys
input = sys.stdin.readline

M, N = map(int, input().split())

primenumber = [False,False] + ([True] * N) 
for i in range(M, N+1):
    if primenumber[i] is True:
        isPrime = True
        # 소수 확인
        for n in range(2, int(i**0.5)+1):
            if i % n == 0:
                isPrime = False
                break
        if isPrime is True: print(i)
        # 소수의 배수는 소수에서 제외
        for j in range(i*2, len(primenumber), i):
            primenumber[j] = False