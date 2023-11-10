import sys
input = sys.stdin.readline
N = int(input())
village = []
for _ in range(N):
    village.append(list(map(int, input().rstrip())))

result = []

def bfs(x, y):
    global home_cnt, village, result
    village[x][y] = -1
    home_cnt += 1
    for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=x+i<N and 0<=y+j<N and village[x+i][y+j] == 1:
            bfs(x+i, y+j)

for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            home_cnt = 0
            bfs(i,j)
            result.append(home_cnt)

print(len(result))
result.sort()
for r in result:
    print(r)