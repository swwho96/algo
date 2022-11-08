import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers_sum = [0]
tmp_sum = 0

for i in numbers:
    tmp_sum += i
    numbers_sum.append(tmp_sum)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(numbers_sum[end] - numbers_sum[start-1])