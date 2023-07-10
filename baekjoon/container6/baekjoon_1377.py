import sys
input = sys.stdin.readline
n = int(input())
array = []
index_dict = {}
for i in range(n):
    p = int(input())
    array.append(p)
    index_dict[p] = i
swap_cnt = 0
array_sort = sorted(array)
for idx, a in enumerate(array_sort):
    if swap_cnt < index_dict[a] - idx:
        swap_cnt = index_dict[a] - idx
print(swap_cnt+1)

# -------------------------------------------

import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append((int(input()), i))

swap_cnt = 0
sorted_a = sorted(a)

for i in range(n):
    if swap_cnt < sorted_a[i][1] - i:
        swap_cnt = sorted_a[i][1] - i
print(swap_cnt + 1)