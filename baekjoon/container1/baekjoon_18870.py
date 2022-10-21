import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers_set = sorted(set(numbers))
idx_dict = {}
for idx, num in enumerate(numbers_set):
    idx_dict[num] = str(idx)
for n in numbers:
    print(idx_dict[n], end=' ')