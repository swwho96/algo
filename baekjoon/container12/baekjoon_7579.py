import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ms = list(map(int, input().split()))
Cs = list(map(int, input().split()))
datas = [[m,c] for m,c in zip(Ms, Cs)]

answer = 10001
volume = sum(Cs)
bags = [[0]*(volume+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = datas[i-1][0], datas[i-1][1]
    for j in range(volume+1):
        if j >= v:
            bags[i][j] = max(bags[i-1][j], bags[i-1][j-v]+w)
        else:
            bags[i][j] = bags[i-1][j]
        if bags[i][j] >= M:
            answer = min(answer, j)

print(answer)