import sys
N, M = map(int, sys.stdin.readline().split())
not_heard = set()
for _ in range(N):
    not_heard.add(sys.stdin.readline().rstrip())
not_heard_not_seen = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in not_heard:
        not_heard_not_seen.append(name)
print(len(not_heard_not_seen))
for name in sorted(not_heard_not_seen):
    print(name)