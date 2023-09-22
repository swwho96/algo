def solution(n):
    answer = []
    if n == 1 : return [1]
    if n == 2 : return [1,2,3]
    # 탑 쌓기
    board = [[1] * i for i in range(1, n+1)]
    # 탑에 숫자 넣기
    flag = True
    row, col = 0, 0
    while flag:
        # 왼쪽 - 아래방향
        while True:
            nrow, ncol = row + 1, col
            if nrow < n and board[nrow][ncol] == 1:
                board[nrow][ncol] = board[row][col] + 1
                row, col = nrow, col
            else:
                break        
        # 아래 - 오른쪽 방향
        while True:
            nrow, ncol = row, col + 1 
            if ncol <= nrow and board[nrow][ncol] == 1:
                board[nrow][ncol] = board[row][col] + 1
                row, col = nrow, ncol
            else:
                break
        # 오른쪽 - 왼쪽 위 방향
        while True:
            nrow, ncol = row - 1, col - 1
            if 0 < nrow and 0 < ncol and board[nrow][ncol] == 1:
                board[nrow][ncol] = board[row][col] + 1
                row, col = nrow, ncol
            else:
                if board[row+1][col] != 1:
                    flag = False
                break
    # 탑의 각 행 모으기
    for b in board:
        answer.extend(b)
    return answer

# ------------------------------------------------------------------------------------------

def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    row, col = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            if angle == 0:
                row += 1
            elif angle == 1:
                col += 1
            elif angle == 2:
                row -= 1
                col -= 1
            res[row][col] = num
            num += 1
    return [j for i in res for j in i]