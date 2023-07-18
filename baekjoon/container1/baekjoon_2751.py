import sys
input = sys.stdin.readline
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for num in numbers:
    print(num)

# -----------------------------------

import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

def merge_sort(s, e):
    if e-s < 1:
        return
    mid = int(s+(e-s) / 2)
    merge_sort(s, mid)
    merge_sort(mid, e)
    