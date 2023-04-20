import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
total_zero = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    total_zero += tmp.count(0)
    board.append(tmp)
result_cnt = total_zero
result_b = board
directions = {
    1: [[(-1,0)], [(1,0)], [(0,-1)], [(0,1)]],
    2: [[(-1,0), (1,0)], [(0,1), (0,-1)]],
    3: [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
    4: [[(0,-1),(-1,0),(0,1)], [(-1,0),(0,1),(1,0)], [(0,1),(1,0),(0,-1)], [(-1,0),(0,-1),(1,0)]],
    5: [[(-1,0), (1,0), (0,-1), (0,1)]]
}

def bfs(b:list, cnt:int, q:list):
    global result_b, result_cnt, total_zero
    if not q:
        if result_cnt > (total_zero-cnt):
            result_cnt = total_zero - cnt
            result_b = b
        return
    x, y = q[0]
    for direct in directions[b[x][y]]:
        tmp_b = copy.deepcopy(b)
        tmp_cnt = cnt
        for d in direct:
            r,c = x,y
            while True:
                nx, ny = r+d[0], c+d[1]
                if 0<=nx<n and 0<=ny<m:
                    if tmp_b[nx][ny] != 6:
                        if tmp_b[nx][ny] == 0:
                            tmp_b[nx][ny] = 9
                            tmp_cnt += 1
                        r, c = nx, ny
                    else:
                        break
                else:
                    break
        bfs(tmp_b, tmp_cnt, q[1:])
    
Q = []
for i in range(n):
    for j in range(m):
        if 0< board[i][j] < 6:
            Q.append((i,j))

bfs(board, 0, Q)
print('cctv 설치 전 사각지대', total_zero)
for p in result_b:
    print(p)
print('cctv 설치 후 사각지대', result_cnt)