# 주어진 범위내의 소수 출력하기
M, N = map(int, input().split())
table = [True] * (N+1)
for i in range(2, int((N+1)**0.5)+1):
    if table[i]:
        for j in range(2*i, (N+1), i):
            table[j] = False

for i in range(M, (N+1)):
    if table[i] and i > 1:
        print(i)