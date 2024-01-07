import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
answer = []

# 소수 구하기
def is_Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for n in range(10**(N-1), 10**(N)):
    str_n = str(n)
    flag = True
    for idx in range(N):
        if is_Prime(int(str_n[:idx+1])) is False:
            flag = False
            break
    if flag is True:
        print(n)