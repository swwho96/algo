import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

# 메모이제이션을 위한 DP 테이블 초기화
dp = [[-1] * N for _ in range(M)]
answer = 0

# DFS 함수 정의
def path_count(r: int, c: int) -> int:
    global answer
    answer += 1
    # 목표 위치에 도달하면 경로의 개수를 1로 반환
    if r == M - 1 and c == N - 1:
        return 1
    
    # 이미 계산된 경우 바로 반환
    if dp[r][c] != -1:
        return dp[r][c]
    
    # 경로의 개수 초기화
    dp[r][c] = 0
    
    # 네 방향으로 이동
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + i, c + j
        
        # 이동할 좌표가 범위 내에 있고, 내리막길인 경우
        if 0 <= nr < M and 0 <= nc < N and board[nr][nc] < board[r][c]:
            dp[r][c] += path_count(nr, nc)
    
    return dp[r][c]

# 시작점에서 DFS 시작
print(path_count(0, 0))