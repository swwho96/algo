n = int(input())
# 소수 판별
def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 신기한 소수 찾기
def dfs(i):
    if isPrime(i) is True:
        if len(str(i)) == n:
            print(i)
            return
        for num in range(1, 10):
            dfs(int(str(i)+str(num)))

dfs(2)
dfs(3)
dfs(5)
dfs(7)