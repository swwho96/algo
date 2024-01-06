'''
정렬 전후 index값의 차이의 최대값은 swap의 횟수와 같다
'''

import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))
A.sort()

answer = 0
for idx, a in enumerate(A):
    num, i = a
    if (i-idx) > answer:
        answer = i-idx

print(answer+1)