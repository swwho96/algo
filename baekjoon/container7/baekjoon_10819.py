from itertools import permutations
N = int(input())
numbers = list(map(int, input().split()))
result = -1000
for combi in permutations(numbers, N):
    tmp = 0
    for i in range(0,N-1):
        tmp += abs(combi[i] - combi[i+1])
    result = max(tmp, result)

print(result)