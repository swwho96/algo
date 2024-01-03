'''
수열의 각 원소에 대해, 가장 가까운 자신보다 큰 수를 찾아 출력한다

'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
q = []
answer = [-1] * N
for i, num in enumerate(A):
    while q and q[-1][1] < num:
        a, b = q.pop()
        answer[a] = num
    q.append([i, num])

print(' '.join(map(str, answer)))