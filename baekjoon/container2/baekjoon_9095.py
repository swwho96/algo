from  itertools import product
from collections import defaultdict
num_combination = defaultdict(int)
for i in range(1,12):
    for c in product([1,2,3], repeat=i):
        num_combination[sum(c)] += 1
T = int(input())
for _ in range(T):
    print(num_combination[int(input())])