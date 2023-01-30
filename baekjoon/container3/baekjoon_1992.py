import sys
input = sys.stdin.readline

N = int(input())
board = []
result = ''
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

def check(x,y,size):
    global board
    flag = board[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[i][j] != flag:
                return False
    return True

def dfs(x,y,size):
    global board
    global result
    if size == 1 or check(x,y,size) is True: # board가 모두 0 혹은 1인 경우
        result += str(board[x][y])
        return
    result += '('
    size //= 2
    tmp = []
    # 1사분면
    dfs(x,y,size)
    # 2사분면
    dfs(x,y+size,size)
    # 3사분면
    dfs(x+size,y,size)
    # 4사분면
    dfs(x+size,y+size,size)
    result += ')'

dfs(0,0,N)
print(result)