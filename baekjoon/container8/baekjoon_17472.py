from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 지도 입력
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 섬 구분 짓기
check_1 = set()
def findIsland(r, c, cnt):
    q = deque([(r,c)])
    board[r][c] = cnt
    check_1.add((r,c))
    while q:
        x, y = q.popleft()
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+i, y+j
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = cnt
                check_1.add((nx,ny))
                q.append((nx,ny))
cnt = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            findIsland(i, j, cnt)
            cnt += 1
cnt -= 1

# 섬과 섬사이 거리 구하기
graph = [[int(10e9)] * (cnt) for _ in range(cnt)]
for i in range(1, cnt):
    graph[i][i] = 0

def makeBridge(r,c,num,length,direction):
    if 0<=r<N and 0<=c<M:
        if length > 0 and board[r][c] == num:
            return
        if board[r][c] > 0 and num != board[r][c]:
            if length-1 < 2:
                return
            end = board[r][c]
            graph[num-1][end-1] = min(length-1, graph[num-1][end-1])
            graph[end-1][num-1] = min(length-1, graph[end-1][num-1])
            return
        return makeBridge(r+direction[0],c+direction[1],num,length+1,direction)
    return

for r, c in check_1:
    n = board[r][c]
    for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=r+i<N and 0<=c+j<M and board[i+r][j+c] != n:
            makeBridge(r, c, n, 0, (i,j))

# 최소 신장 트리 구하기
def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

parent = [i for i in range(cnt)]
heap = []
for i in range(1, cnt):
    for j in range(i, cnt):
        heappush(heap, (graph[i][j], i, j))

total_bridge_length = 0
while heap:
    cost, a, b = heappop(heap)
    if find(a,parent) != find(b, parent):
        union(a, b, parent)
        total_bridge_length += cost

print(total_bridge_length if total_bridge_length < int(10e9) else -1)