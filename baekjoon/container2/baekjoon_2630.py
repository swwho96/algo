from collections import deque
import sys
input = sys.stdin.readline
def check(b):
    n = len(b)
    if n == 1:
        return True
    tmp = b[0][0]
    for i in range(n):
        for j in range(n):
            if b[i][j] != tmp:
                return False
    return True 


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
color = [0, 0]
q = deque([board])
while q:
    nb = q.popleft()
    if check(nb) is True:
        color[nb[0][0]] += 1
    else:
        n_half = len(nb) // 2
        startpoint = [(0,0), (0,n_half), (n_half,0), (n_half, n_half)]
        for point in startpoint:
            nb_slice = []
            for i in range(n_half):
                nb_slice.append(nb[point[0]+i][point[1]:point[1]+n_half])
            q.append(nb_slice)

print(color[0])
print(color[1])