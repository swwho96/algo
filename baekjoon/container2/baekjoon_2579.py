import sys
N  = int(sys.stdin.readline().rstrip())
stairs = list(map(int, sys.stdin.read().splitlines()))
if N <= 2:
    print(sum(stairs))
else:
    score = [0] * 300
    score[0] = stairs[0]
    score[1] = max(stairs[0]+stairs[1], stairs[1])
    for i in range(2, N):
        score[i] = max(score[i-3]+stairs[i-1]+stairs[i], score[i-2]+stairs[i])
    print(score[N-1])