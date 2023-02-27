n = int(input())
result = 0
board = [0] * n
visited = [False] * n

def queen(row):
    global result
    if row == n:
        result += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        board[row] = i
        if check(row):
            visited[i] = True
            queen(row+1)
            visited[i] = False

def check(row):
    for i in range(row):
        if (board[row] == board[i]) or (abs(row-i) == abs(board[row]-board[i])):
            return False
    return True

queen(0)
print(result)