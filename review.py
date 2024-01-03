'''
수열의 각 원소에 대해, 가장 가까운 자신보다 큰 수를 찾아 출력한다

'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
q = []
answer = [-1] * N
for i in range(N):
    while q and A[q[-1]] < A[i]:
        tmp = q.pop()
        answer[tmp] = A[i]
    q.append(i)

print(' '.join(map(str, answer)))