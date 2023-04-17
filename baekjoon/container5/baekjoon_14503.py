import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r,c,d = map(int, input().split())
clean_cnt = 0
direct = [[-1,0],[0,1],[1,0],[0,-1]]
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[r][c] == 0:
        clean_cnt += 1
        board[r][c] = 9
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    # 반시계 방향으로 90 회전을 반복하여 빈칸으로 이동한다.
    flag = False
    for _ in range(4):
        d = (d-1) if d > 0 else 3
        nx, ny = r+direct[d][0], c+direct[d][1]
        if 0<=nx<n and 0<=ny<m  and board[nx][ny] == 0:
            r, c = nx, ny
            flag = True
            break
    if flag is False:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진한다
        nx, ny = r-direct[d][0], c-direct[d][1]
        if 0<=nx<n and 0<=ny<m  and board[nx][ny] != 1:
            r, c = nx, ny
        # 바라보는 방향의 뒤 쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
        else:
            break
print(clean_cnt)