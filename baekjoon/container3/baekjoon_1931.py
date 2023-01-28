from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
q = deque([])
result = []
for _ in range(N):
    s, e = map(int, input().split())
    q.append((s,e))
q = deque(sorted(q, key=lambda x: (x[0], x[1])))
result.append(q.popleft())
while q:
    schedule = q.popleft()
    if result:
        if result[-1][0] <= result[-1][1] <= schedule[0] <= schedule[1]:
            result.append(schedule)
        elif result[-1][0] < schedule[0] <= schedule[1] < result[-1][1]:
            result.pop()
            result.append(schedule)
    else:
        result.append(schedule)

print(result)
print(len(result))