import sys
from collections import deque
input = sys.stdin.readline

class BeadGame:
    def __init__(self, board:list, N:int, M:int):
        self.board = board
        self.limit = 10 # 이동이 10번을 초과하면 구슬 탈출 실패
        self.N, self.M = N, M
        self.visited = set()
        self.direction = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(N):
            for j in range(M):
                if self.board[i][j] == 'R':
                    self.R = [i,j]
                elif self.board[i][j] == 'B':
                    self.B = [i,j]
    
    def move(self, r:int, c:int, d:int):
        nr, nc = r, c
        while True:
            nr += self.direction[d][0]
            nc += self.direction[d][1]
            if self.board[nr][nc] == '#':
                nr -= self.direction[d][0]
                nc -= self.direction[d][1]
                break
            if self.board[nr][nc] == 'O':
                return nr, nc, True
        return nr, nc, False
    
    def game(self):
        q = deque([(self.R, self.B, 0)]) # R, B, move_cnt
        self.visited.add((self.R[0], self.R[1], self.B[0], self.B[1]))

        while q:
            r, b, cnt = q.popleft()
            if cnt >= self.limit:
                break

            for i in range(4):
                nrR, ncR, Rhole = self.move(r[0], r[1], i)
                nrB, ncB, Bhole = self.move(b[0], b[1], i)
                
                if Bhole:
                    continue
                if Rhole:
                    return cnt+1
                
                if nrR == nrB and ncR == ncB:
                    if abs(nrR-r[0])+abs(ncR-r[1]) > abs(nrB-b[0])+abs(ncB-b[1]):
                        nrR -= self.direction[i][0]
                        ncR -= self.direction[i][1]
                    else:
                        nrB -= self.direction[i][0]
                        ncB -= self.direction[i][1]
                
                if (nrR, ncR, nrB, ncB) not in self.visited:
                    self.visited.add((nrR, ncR, nrB, ncB))
                    q.append(((nrR, ncR), (nrB, ncB), cnt+1))
        return -1
        


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))
result = BeadGame(board, N, M).game()
print(result)