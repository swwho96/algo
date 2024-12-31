import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
things = list(map(int, input().split()))
answer = 0

list_A = things[:(N//2)]
list_B = things[(N//2):]

a_combi_list = []
b_combi_list = []

for n in range(len(list_A)+1):
    combi_a = combinations(list_A, n)
    for combi in combi_a:
        a_combi_list.append(sum(combi))

for n in range(len(list_B)+1):
    combi_b = combinations(list_B, n)
    for combi in combi_b:
        b_combi_list.append(sum(combi))

a_combi_list.sort()

for b in b_combi_list:
    if b > C:
        continue
    left, right = 0, len(a_combi_list)
    while left < right:
        mid = (left+right) // 2
        if a_combi_list[mid] + b <= C:
            left = mid+1
        else:
            right = mid
    answer += right

print(answer)