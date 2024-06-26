import sys
input = sys.stdin.readline
board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

# 빈칸 위치 확인
blank_locations = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank_locations.append((i, j))

# 스도쿠 확인 함수
def is_valid(x, y, num):
    # 가로 확인
    if num in board[x]:
        return False
    # 세로 확인
    for i in range(9):
        if board[i][y] == num:
            return False
    # 3x3 사각형 확인
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] == num:
                return False
    return True

# 빈칸 채우는 함수 구현
def fill(idx):
    if idx == len(blank_locations):
        for b in board:
            print(' '.join(map(str, b)))
        exit()
    
    x, y = blank_locations[idx]
    for i in range(1, 10):
        if is_valid(x, y, i):
            board[x][y] = i
            fill(idx + 1)
            board[x][y] = 0

fill(0)