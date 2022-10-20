import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort(reverse=True)
print(numbers[K-1])