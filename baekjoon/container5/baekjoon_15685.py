import sys
input = sys.stdin.readline
board = [[0]*101 for _ in range(101)]
n = int(input())
direct = [(0,1), (-1,0), (0,-1), (1,0)]
result = 0

def check():
    global result
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                result += 1

def dragon(g:int, x:int, y:int, q:list):
    global k
    tmp = []
    if g == k:
        for i in q:
            board[x][y] = 1
            x, y = x+direct[i][0], y+direct[i][1]
        board[x][y] = 1
        return
    for i in q:
        i = (i+1) % 4
        tmp.append(i)
    return dragon(g+1, x, y, (q+tmp[::-1]))

for _ in range(n):
    x, y, d, k = map(int, input().split())
    dragon(0, y, x, [d])

check()
print(result)

