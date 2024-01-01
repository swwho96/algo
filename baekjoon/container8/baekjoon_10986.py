import sys
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
IDXS = [0] * M
S[0] = A[0]
answer = 0
for i in range(1,N):
    S.append(S[-1]+A[i])

for i in range(N):
    tmp = S[i] % M
    if tmp == 0:
        answer += 1
    IDXS[tmp] += 1

for i in range(M):
    if IDXS[i] > 1:
        answer += (IDXS[i]*(IDXS[i]-1)) // 2

print(answer)