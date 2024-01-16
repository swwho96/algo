import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
roots = list(map(int, input().split()))

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

parent = [i for i in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            union(i, j, parent)

flag = set()
for r in roots:
    flag.add(parent[r-1])
print('YES' if len(flag) == 1 else 'NO')