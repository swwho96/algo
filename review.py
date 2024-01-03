''''
1부터 N까지 숫자를 하나씩 스택에 담거나 빼면서, 주어진 수열을 만든다
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = deque([])
for _ in range(N):
    A.append(int(input()))

q = deque([])
answer = []
i = 1
while A:
    if q and A[0] == q[-1]:
        answer.append('-')
        q.pop()
        A.popleft()
    elif q and q[-1] > A[0]:
        answer = ['NO']
        break
    else:
        q.append(i)
        i += 1
        answer.append('+')

for a in answer:
    print(a)