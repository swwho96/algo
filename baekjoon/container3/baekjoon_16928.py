import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

up_down = {}
for _ in range(N+M):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    up_down[s] = e

visited = [False] * 101
board = [0] * 101

q = [1]
while q:
    now = q.pop(0)
    for i in range(1, 7):
        _now = now + i
        if 0<= _now <=100:
            if _now in up_down:
                _now = up_down[_now]
            if not visited[_now]:
                visited[_now] = True
                board[_now] = board[now] + 1
                q.append(_now)

print(board[100])