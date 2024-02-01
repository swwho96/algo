import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input()) # 층
    N = int(input()) # 호
    apt = [[1] * (N+1) for _ in range(K+1)]
    # 0층 i호는 i명 거주
    for i in range(1, N+1):
        apt[0][i] = i
    # a층 b호는 a-1층 1호부터 b호까지의 총 인원
    for a in range(1, K+1):
        for b in range(2, N+1):
            apt[a][b] = apt[a][b-1] + apt[a-1][b]
    # K층 N호 인원
    print(apt[K][N])