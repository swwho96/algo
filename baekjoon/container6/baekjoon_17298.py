from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
# temp를 순회하면서 Ai 보다 작은 수들의 NGE를 Ai로 수정
# Ai-1 < Ai 인 경우, NGE는 Ai
# Ai-1 >= Ai 인 경우, temp에 저장

temp = []
result = [0] * n
for i in range(n):
    while temp and A[temp[-1]] < A[i]:
        result[temp.pop()] = A[i]
    temp.append(i)
while temp:
    result[(temp.pop())] = -1
print(' '.join(map(str, result)))