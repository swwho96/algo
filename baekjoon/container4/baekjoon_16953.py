from collections import deque
a, b = map(int, input().split())
q = deque([(0, a)])
visited = set()
result = -1
while q:
    cnt, n = q.popleft()
    if n == b:
        result = cnt+1
        break
    tmp = n*2
    if tmp not in visited and tmp <= b:
        q.append((cnt+1, tmp))
        visited.add(tmp)
    tmp = n*10 + 1
    if tmp not in visited and tmp <= b:
        q.append((cnt+1, tmp))
        visited.add(tmp)
print(result)