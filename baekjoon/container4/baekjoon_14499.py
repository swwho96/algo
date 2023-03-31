import sys
input = sys.stdin.readline
n,m,x,y,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
operations = list(map(int, input().split()))

def turn(t:int, dice:list)->list:
    if t == 1:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    if t == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    if t == 3:    
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    if t == 4:    
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    return dice

dice = [0,0,0,0,0,0]
moves = [(0,1),(0,-1),(-1,0),(1,0)]
for op in operations:
    nx, ny = x + moves[op-1][0], y + moves[op-1][1]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
        dice = turn(op, dice)
        if graph[x][y] == 0:
            graph[x][y] = dice[-1]
        else:
            dice[-1] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])
