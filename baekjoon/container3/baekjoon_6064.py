import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m,n,x,y = map(int, input().split())
    k = x
    result = -1
    while k<=m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            result = k
            break
        k += m
    print(result)